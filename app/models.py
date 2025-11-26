# Key SQLAlchemy imports you'll need:
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base  # This we already have

class User(Base):
    __tablename__ = "users"  # This tells SQLAlchemy what to name the table in the database

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class VocabularyItem(Base):
    __tablename__ = "vocabulary_items"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    term_id = Column(Integer, ForeignKey("terms.id"), nullable=False, index=True)
    review_count = Column(Integer, default=0)
    saved_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_score = Column(Integer, nullable=True)
    term = relationship("Term", backref="vocab_items")

class Term(Base):
    __tablename__ = "terms"
    
    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, unique=True, nullable=False, index=True)

    # NEW FIELD – foreign key to categories table
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    # keep these for now, we will delete later
    category = Column(String, nullable=False, index=True)

    formal_definition = Column(String, nullable=False)
    example = Column(String, nullable=True)
    simple_definition = Column(String, nullable=False)
    why_it_matters = Column(String, nullable=True)  
    difficulty = Column(Integer, nullable=False, default=1)  
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)  # "networking", "devops", etc.
    description = Column(String, nullable=True)

    # we'll wire up relationships later

class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    term_id = Column(Integer, ForeignKey("terms.id"), nullable=False)
    user_answer = Column(String, nullable=False)
    score = Column(Integer, nullable=False)  # 0-100
    ai_feedback = Column(String, nullable=True)
    correct_answer = Column(String, nullable=True)
    attempted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

