from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..services import ingest_service
from ..schemas.ingest import DirectNumericIngest, DirectTextIngest
from ..security.jwt import get_current_admin_user

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/numeric")
def ingest_numeric(
    payload: DirectNumericIngest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    """Push a single numeric record."""
    return ingest_service.ingest_numeric_single(db, payload)

@router.post("/text")
def ingest_text(
    payload: DirectTextIngest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_admin_user)
):
    """Push a single text record."""
    return ingest_service.ingest_text_single(db, payload)
