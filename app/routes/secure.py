from fastapi import APIRouter, Depends
from app.services.auth import get_current_user

router = APIRouter()

@router.get("/secure-data")
async def secure_data(user: dict = Depends(get_current_user)):
    return {"message": "Acesso autorizado", "user": user}
