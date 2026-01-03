from fastapi import FastAPI
from todo import models
from todo.database import engine
from todo.routes import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth.router)
app.include_router(todos.router)