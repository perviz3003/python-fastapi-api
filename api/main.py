from fastapi import FastAPI
from . import models, database
from .routers import user, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(router=auth.router)
app.include_router(router=user.router)
