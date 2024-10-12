from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Directory(Base):
    __tablename__ = 'directories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    files = relationship('File', back_populates='directory', cascade='all, delete-orphan')

    @property
    def update_time(self):
        if self.files:
            return max(file.update_time for file in self.files)
        return None

    def __repr__(self):
        return f"<Directory(id='{self.id}', update_time='{self.update_time}')>"

    def search_files(self, search_string):
        return [file for file in self.files if search_string in file.file_path]

class File(Base):
    __tablename__ = 'files'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String, nullable=False, unique=True)
    hash = Column(String, nullable=False)
    update_time = Column(DateTime, default=datetime.datetime.utcnow)
    directory_id = Column(Integer, ForeignKey('directories.id'))
    directory = relationship('Directory', back_populates='files')

    def __repr__(self):
        return f"<File(file_path='{self.file_path}', hash='{self.hash}', update_time='{self.update_time}', directory_id='{self.directory_id}')>"