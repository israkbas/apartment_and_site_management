from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum
from datetime import datetime

Base = declarative_base()

class IncomeType(str, enum.Enum):
    AIDAT = "AIDAT"
    KIRA = "KIRA"
    DIGER = "DIGER"

class ExpenseType(str, enum.Enum):
    ELEKTRIK = "ELEKTRIK"
    SU = "SU"
    TEMIZLIK_MALZEME = "TEMIZLIK_MALZEME"
    BAKIM_ONARIM = "BAKIM_ONARIM"
    TESISATCI = "TESISATCI"
    TEMIZLIKCI = "TEMIZLIKCI"
    DIGER = "DIGER"

class Apartment(Base):
    __tablename__ = "apartments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    
    incomes = relationship("Income", back_populates="apartment")
    expenses = relationship("Expense", back_populates="apartment")

class Income(Base):
    __tablename__ = "incomes"
    
    id = Column(Integer, primary_key=True, index=True)
    apartment_id = Column(Integer, ForeignKey("apartments.id"))
    amount = Column(Float)
    description = Column(String)
    date = Column(DateTime, default=datetime.now)
    income_type = Column(Enum(IncomeType))
    
    apartment = relationship("Apartment", back_populates="incomes")

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    apartment_id = Column(Integer, ForeignKey("apartments.id"))
    amount = Column(Float)
    description = Column(String)
    date = Column(DateTime, default=datetime.now)
    expense_type = Column(Enum(ExpenseType))
    
    apartment = relationship("Apartment", back_populates="expenses")