from fastapi import FastAPI,Depends, HTTPException,Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
# from .database import SessionLocal, engine, Base, init_db
# from .database import models, schemas, crud
from .database.database import init_db, SessionLocal, engine, Base
from .database import models, schemas, crud
from fastapi.responses import HTMLResponse
init_db()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/reg",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)