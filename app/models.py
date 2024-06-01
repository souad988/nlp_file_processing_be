from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.db_config import Base

class FileUpload(Base):
    __tablename__ = "file_uploads"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def save(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)