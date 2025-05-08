from fastapi import FastAPI
from init.db import connectToDb
from init.settings import settings
from init.setRoutes import setRoutes

app = FastAPI()
connectToDb(settings.databaseName)
setRoutes(app)