from datetime import date as Date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# --- Schémas ---


class TransactionIn(BaseModel):
    date: Date
    libelle: str
    montant: int
    compte: str


class Transaction(TransactionIn):
    id: int


# --- Application et stockage en mémoire ---

app = FastAPI()
transactions: list[Transaction] = []
next_id = 1


def trouver(transaction_id: int) -> Transaction:
    for t in transactions:
        if t.id == transaction_id:
            return t
    raise HTTPException(status_code=404, detail="Transaction introuvable")


# --- Routes ---


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/transactions", status_code=201, response_model=Transaction)
def create_transaction(transaction: TransactionIn):
    global next_id
    new = Transaction(id=next_id, **transaction.model_dump())
    next_id += 1
    transactions.append(new)
    return new


@app.get("/transactions", response_model=list[Transaction])
def list_transactions():
    return transactions


@app.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int):
    return trouver(transaction_id)


@app.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: int, transaction: TransactionIn):
    ancienne = trouver(transaction_id)
    position = transactions.index(ancienne)
    maj = Transaction(id=transaction_id, **transaction.model_dump())
    transactions[position] = maj
    return maj


@app.delete("/transactions/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: int):
    transactions.remove(trouver(transaction_id))
