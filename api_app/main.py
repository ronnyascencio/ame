from fastapi import FastAPI
from .routers import users, reviews, search, auth
from .database.database import engine
from .models.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/health")
async def root():
    return {"message": "health check"}


""" routers api """
app.include_router(users.router)
app.include_router(reviews.router)
app.include_router(search.router)
app.include_router(auth.router)
