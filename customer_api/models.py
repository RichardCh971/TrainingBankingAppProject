from pydantic import BaseModel
from typing import List

class Account(BaseModel):
    id: int
    type: str
    balance: float

class Customer(BaseModel):
    id: int 
    name: str
    accounts: List[Account]

class CustomerUpdate(BaseModel):
    name: str

class AccountUpdate(BaseModel):
    type: str
    balance: float