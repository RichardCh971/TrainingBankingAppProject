from pydantic import BaseModel
from typing import List, Optional

class Account(BaseModel):
    id: int
    type: str
    balance: float

class Customer(BaseModel):
    id: int
    username: Optional[str] = None
    name: str
    accounts: List[Account]

class CustomerUpdate(BaseModel):
    name: str

class AccountUpdate(BaseModel):
    type: str
    balance: float

class AccountCreate(BaseModel):
    type: str
    balance: float