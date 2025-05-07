from fastapi import FastAPI, HTTPException
from typing import List
from database import create_db_and_tables, engine , DATABASE_URL
from models.items import Item  # Import from models.py
from sqlmodel import Session, select, create_engine, SQLModel
import os
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine
    engine = create_engine(url=DATABASE_URL, echo=True) # Assurer le démarrage de la base de données principale
    await create_db_and_tables()
    yield
    SQLModel.metadata.drop_all(engine) # Nettoyage à l'arrêt (pour les tests, cela ne sera peut-être pas nécessaire pour la production)

app = FastAPI(lifespan=lifespan)

@app.get("/items", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

@app.post("/items", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    with Session(engine) as session:
        db_item = session.get(Item, item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        item_data = item.dict(exclude_unset=True)
        for key, value in item_data.items():
            setattr(db_item, key, value)
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return {"ok": True}