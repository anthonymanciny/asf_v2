from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.depends import get_db
from app.models.models import Pessoa
from app.schemas.validation import LoginSchema, Token
from app.auth.hashing import verify_password, get_password_hash
from app.auth.jwt import create_access_token
from datetime import timedelta
from app.db.connection import ACCESS_TOKEN_EXPIRE_MINUTES

auth_router = APIRouter()

@auth_router.post("/login", response_model=Token)
def login(user: LoginSchema, db: Session = Depends(get_db)):
    pessoa = db.query(Pessoa).filter(Pessoa.email == user.email).first()
    if not pessoa or not verify_password(user.senha, pessoa.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": pessoa.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
