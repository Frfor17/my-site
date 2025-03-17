from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud


app = FastAPI()

@app.get("/getmessage")
def read_messages(db: Session = Depends(get_db)):
    return crud.get_messages(db)