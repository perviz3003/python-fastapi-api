from fastapi import FastAPI
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
