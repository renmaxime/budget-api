from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date as Date

app = FastAPI()
transactions = []

@app.get("/health")
def health():
    return {"status":"ok"}

class TransactionIn(BaseModel):
    date : Date
    libelle : str
    montant : int
    compte : str

class Transaction(TransactionIn):
    id : int

@app.post("/transactions", status_code=201,response_model=Transaction)
def create_transaction(transaction: TransactionIn):
    next_id = len(transactions) + 1
    new = Transaction(id = next_id, **transaction.model_dump())
    transactions.append(new)
    return new

@app.get("/transactions", response_model=list[Transaction])
def list_transactions():
    return transactions