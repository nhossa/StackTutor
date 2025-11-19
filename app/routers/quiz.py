"""
Quiz Router - Handles quiz generation and answer grading
"""
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from zoneinfo import ZoneInfo

from app.schemas import QuizQuestion, QuizAnswerRequest, QuizResult
from app.database import get_db
from app.models import Term, QuizAttempt

# Create router instance
router = APIRouter(
    prefix="/quiz",
    tags=["quiz"]
)


@router.get("/random", response_model=QuizQuestion)
async def get_random_quiz(db: Session = Depends(get_db)):
    """
    Get a random term to quiz on
    """
    # Get random term from database using SQLite's random()
    random_term = db.query(Term).order_by(func.random()).first()
    
    if not random_term:
        raise HTTPException(
            status_code=404,
            detail="No terms available in database. Please add terms first."
        )
    
    return QuizQuestion(
        term_id=random_term.id,
        term=f"Explain {random_term.term}",
        category=random_term.category
    )


@router.post("/answer", response_model=QuizResult)
async def submit_answer(answer: QuizAnswerRequest, db: Session = Depends(get_db)):
    """
    Submit quiz answer and get AI grading
    """
    # Get the term from database
    term = db.query(Term).filter(Term.id == answer.term_id).first()
    
    if not term:
        raise HTTPException(
            status_code=404,
            detail=f"Term with id {answer.term_id} not found"
        )
    
    # Placeholder score (will add AI grading later)
    score = 50
    feedback = "AI grading coming soon!"
    saved = False
    
    # Save quiz attempt to database
    quiz_attempt = QuizAttempt(
        user_id=None,  # Will add after authentication
        term_id=answer.term_id,
        user_answer=answer.user_answer,
        score=score,
        ai_feedback=feedback,
        correct_answer=term.simple_definition
    )
    
    db.add(quiz_attempt)
    db.commit()
    
    return QuizResult(
        term=term.term,
        score=score,
        feedback=feedback,
        correct_answer=term.simple_definition,
        your_answer=answer.user_answer,
        saved_to_vocabulary=saved
    )
