import os
import pickle
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

class PDFProcessor:
    def __init__(self):
        load_dotenv()
        # Set your OpenAI API key
        self.api_key = os.getenv("OPENAI_KEY")
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=self.api_key)
        self.embedding = OpenAIEmbeddings(openai_api_key=self.api_key)

    def load_documents(self, file_paths):
        loaders = [PyPDFLoader(path) for path in file_paths]
        documents = []
        for loader in loaders:
            documents.extend(loader.load())
        return documents
    
    def split_documents(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        return text_splitter.split_documents(documents)
    def get_vector_store(self, document_id):
        chroma_directory = f"uploads/chroma/{document_id}/"
        if os.path.exists(chroma_directory):
            # Load the Chroma instance from the directory
            chroma = Chroma(persist_directory=chroma_directory, embedding_function=self.embedding)
            return chroma
        else:
            raise FileNotFoundError(f"Chroma directory for document {document_id} does not exist.")

    def create_vector_store(self, document_id, splits):
        persist_directory = f'uploads/chroma/{document_id}/'
        chroma = Chroma.from_documents(
            documents=splits,
            embedding=self.embedding,
            persist_directory=persist_directory
        )
        return chroma
    
    def initialize_qa_chain(self, vectordb): 
        return RetrievalQA.from_chain_type(
            self.llm,
            retriever=vectordb.as_retriever()
        )
    
    def answer_question(self, qa_chain, question):
        result = qa_chain({"query": question})
        return result["result"]
