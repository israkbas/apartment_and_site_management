from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from models import IncomeType, ExpenseType

class ApartmentBase(BaseModel):
    name: str
    address: str

class ApartmentCreate(ApartmentBase):
    pass

class Apartment(ApartmentBase):
    id: int
    
    class Config:
        orm_mode = True

class IncomeBase(BaseModel):
    amount: float
    description: str
    income_type: IncomeType
    date: Optional[datetime] = None

class IncomeCreate(IncomeBase):
    apartment_id: int

class Income(IncomeBase):
    id: int
    apartment_id: int
    
    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    amount: float
    description: str
    expense_type: ExpenseType
    date: Optional[datetime] = None

class ExpenseCreate(ExpenseBase):
    apartment_id: int

class Expense(ExpenseBase):
    id: int
    apartment_id: int
    
    class Config:
        orm_mode = True

class ApartmentWithDetails(Apartment):
    incomes: List[Income] = []
    expenses: List[Expense] = []
    
    class Config:
        orm_mode = True