from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timezone

Base = declarative_base()

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo = True)
sessionLocal = sessionmaker(bind = engine)

class Post(Base):
    __tablename__ = "posts" 
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable= False)
    content =Column (String, nullable=False)
    created = Column(DateTime, default=datetime.now(timezone.utc))

Base.metadata.create_all(bind =engine)
