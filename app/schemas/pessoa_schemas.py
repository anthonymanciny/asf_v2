from pydantic import BaseModel
from typing import Optional
from datetime import date

class PessoaBase(BaseModel):
    nome: str
    email: str
    celular: str
    telefone: Optional[str] = None
    cpf: str
    data_nascimento: date
    genero: Optional[str] = None

    class Config:
        orm_mode = True


class PessoaCreate(PessoaBase):
    senha: str  # Será tratado no backend, não enviando em texto simples


class PessoaUpdate(PessoaBase):
    pass

class LoginSchema(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str

class PessoaResponse(PessoaBase):
    id_pessoa: int

    class Config:
        orm_mode = True
