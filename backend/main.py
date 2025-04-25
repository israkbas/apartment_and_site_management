from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Apartman Yönetim Sistemi")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Veya tüm kaynaklara izin vermek için ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Apartment endpoints
@app.post("/apartments/", response_model=schemas.Apartment)
def create_apartment(apartment: schemas.ApartmentCreate, db: Session = Depends(get_db)):
    db_apartment = models.Apartment(name=apartment.name, address=apartment.address)
    db.add(db_apartment)
    db.commit()
    db.refresh(db_apartment)
    return db_apartment

@app.get("/apartments/", response_model=List[schemas.Apartment])
def get_apartments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    apartments = db.query(models.Apartment).offset(skip).limit(limit).all()
    return apartments

@app.get("/apartments/{apartment_id}", response_model=schemas.ApartmentWithDetails)
def get_apartment(apartment_id: int, db: Session = Depends(get_db)):
    apartment = db.query(models.Apartment).filter(models.Apartment.id == apartment_id).first()
    if apartment is None:
        raise HTTPException(status_code=404, detail="Apartman bulunamadı")
    return apartment

# Income endpoints
@app.post("/incomes/", response_model=schemas.Income)
def create_income(income: schemas.IncomeCreate, db: Session = Depends(get_db)):
    db_income = models.Income(**income.dict())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

@app.get("/incomes/", response_model=List[schemas.Income])
def get_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    incomes = db.query(models.Income).offset(skip).limit(limit).all()
    return incomes

@app.get("/apartments/{apartment_id}/incomes", response_model=List[schemas.Income])
def get_apartment_incomes(apartment_id: int, db: Session = Depends(get_db)):
    apartment = db.query(models.Apartment).filter(models.Apartment.id == apartment_id).first()
    if apartment is None:
        raise HTTPException(status_code=404, detail="Apartman bulunamadı")
    return apartment.incomes

# Expense endpoints
@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses/", response_model=List[schemas.Expense])
def get_expenses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).offset(skip).limit(limit).all()
    return expenses

@app.get("/apartments/{apartment_id}/expenses", response_model=List[schemas.Expense])
def get_apartment_expenses(apartment_id: int, db: Session = Depends(get_db)):
    apartment = db.query(models.Apartment).filter(models.Apartment.id == apartment_id).first()
    if apartment is None:
        raise HTTPException(status_code=404, detail="Apartman bulunamadı")
    return apartment.expenses

# Summary endpoints
@app.get("/apartments/{apartment_id}/summary")
def get_apartment_summary(apartment_id: int, db: Session = Depends(get_db)):
    apartment = db.query(models.Apartment).filter(models.Apartment.id == apartment_id).first()
    if apartment is None:
        raise HTTPException(status_code=404, detail="Apartman bulunamadı")
    
    total_income = sum(income.amount for income in apartment.incomes)
    total_expense = sum(expense.amount for expense in apartment.expenses)
    
    return {
        "apartment": apartment.name,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }