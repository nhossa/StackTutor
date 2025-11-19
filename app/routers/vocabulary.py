"""
Vocabulary Router - Handles user's saved terms
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import VocabularyItemResponse, VocabularyListResponse
from app.database import get_db
from app.models import VocabularyItem, Term

# Create router instance
router = APIRouter(
    prefix="/vocabulary",
    tags=["vocabulary"]
)


@router.get("/", response_model=VocabularyListResponse)
async def get_vocabulary(db: Session = Depends(get_db)):
    """
    Get all saved vocabulary items for user
    """
    # TODO: Add user_id filter after authentication
    return {"items": [], "total": 0}
