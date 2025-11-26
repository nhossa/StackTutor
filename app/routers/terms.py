"""
Terms Router - Handles term explanation/lookup
"""
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import TermRequest, TermResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Term
from zoneinfo import ZoneInfo

# Create router instance
router = APIRouter(
    prefix="/terms",
    tags=["terms"]
)

#output validation through TermResponse
@router.post("/", response_model=TermResponse)
async def explain_term(
    request: TermRequest,
    db: Session = Depends(get_db)
):
    """
    Explain a technical term
    """
    # Query database for the term
    term = db.query(Term).filter(Term.term.ilike(request.term)).first()
    
    if not term:
        raise HTTPException(
            status_code=404,
            detail=f"Term '{request.term}' not found in database"
        )
    
    return TermResponse(
        id=term.id,
        term=term.term,
        formal_definition=term.formal_definition,
        simple_definition=term.simple_definition,
        example=term.example,
        why_it_matters=term.why_it_matters,
        category=term.category,
        category_id=term.category_id,
        difficulty=term.difficulty,
        created_at=term.created_at,
    )