from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_connection, create_table
from logic import BankAccount

app = FastAPI(title="Bank Account API")
create_table()

class RegisterRequest(BaseModel):
    accno: int
    name: str

class AmountRequest(BaseModel):
    amount: int


@app.post("/register")
def register_user(data: RegisterRequest):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM accounts WHERE accno=?", (data.accno,))
    if cur.fetchone():
        raise HTTPException(status_code=400, detail="Account already exists")

    cur.execute(
        "INSERT INTO accounts VALUES (?, ?, ?)",
        (data.accno, data.name, 0)
    )
    conn.commit()
    conn.close()

    return {"message": "Account created successfully"}


@app.get("/account/{accno}")
def get_account(accno: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM accounts WHERE accno=?", (accno,))
    row = cur.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Account not found")

    return {"accno": row[0], "name": row[1], "balance": row[2]}


@app.post("/deposit/{accno}")
def deposit(accno: int, data: AmountRequest):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM accounts WHERE accno=?", (accno,))
    row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Account not found")

    account = BankAccount(*row)

    try:
        account.credit(data.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    cur.execute(
        "UPDATE accounts SET balance=? WHERE accno=?",
        (account.balance, accno)
    )
    conn.commit()
    conn.close()

    return {"balance": account.balance}


@app.post("/withdraw/{accno}")
def withdraw(accno: int, data: AmountRequest):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM accounts WHERE accno=?", (accno,))
    row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Account not found")

    account = BankAccount(*row)

    try:
        account.debit(data.amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    cur.execute(
        "UPDATE accounts SET balance=? WHERE accno=?",
        (account.balance, accno)
    )
    conn.commit()
    conn.close()

    return {"balance": account.balance}
