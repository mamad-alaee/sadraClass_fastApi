from fastapi import FastAPI,Request
from init.db import connectToDb
from init.settings import settings
from init.setRoutes import setRoutes
from init.schedular import set_scheduler
from init.loggerSetup import setup_log_for_project
from init.setMiddleWare import middelWareSetter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
connectToDb(settings.databaseName)
logger = setup_log_for_project()
setRoutes(app)
set_scheduler()
middelWareSetter(app,logger)



