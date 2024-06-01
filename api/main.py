import shutil
import time
from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pathlib import Path
from sqlalchemy.orm import Session
from app.db_config import SessionLocal, engine
from app import models
from app.file_processing.pdf_processing import PDFProcessor


app = FastAPI()
processor = PDFProcessor() 

# Define allowed origins
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    # Add other origins as needed
]

# Add the CORS middleware to the application.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers
)




models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






@app.get("/")
def root():
    return {"message": "hello from be!"}

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Define the upload directory
        upload_dir = Path("uploads")
        upload_dir.mkdir(exist_ok=True)
        
        # Define the path to save the uploaded file
        file_location = upload_dir / file.filename
        
        # Save the uploaded file to the defined location
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        time.sleep(1)

        file_record = models.FileUpload(file_name=file.filename)
        file_record.save(db)
        
        # Load documents
        docs = processor.load_documents([str(file_location)])
        
        # Split documents
        splits = processor.split_documents(docs)
        
        # Create vector store
        processor.create_vector_store(document_id = file.filename, splits = splits)  #
        
        
        # Return a success message with file details
        return JSONResponse(content={"file": {"filename":file.filename, "id": file_record.id}, "message": "File uploaded successfully"})
    except Exception as e:
        # Handle any exceptions that occur during file upload
        return JSONResponse(content={"error": str(e)}, status_code=500)
    


# Define request body model
class QuestionAnswerRequest(BaseModel):
    question: str
    filename: str

# Define response model
class QuestionAnswerResponse(BaseModel):
    answer: str


# Define endpoint for question answering
@app.post("/question-answer", response_model=QuestionAnswerResponse)
async def question_answer(qa_request: QuestionAnswerRequest):
    try:
        # Load documents
        docs = processor.load_documents(["uploads/"+qa_request.filename])
        
        # Split documents
        splits = processor.split_documents(docs)
        
        # Create vector store
        #vectordb = processor.create_vector_store(splits)
        
        vectordb = processor.get_vector_store(document_id= qa_request.filename)
        # Initialize QA chain
        qa_chain = processor.initialize_qa_chain(vectordb)
        
        # Answer question
        answer = processor.answer_question(qa_chain, qa_request.question)
        
        return JSONResponse(content={"answer": answer, "message": "question answered successfully"})
    except Exception as e:
        # Handle any exceptions that occur during file upload
        return JSONResponse(content={"error": str(e)}, status_code=500)