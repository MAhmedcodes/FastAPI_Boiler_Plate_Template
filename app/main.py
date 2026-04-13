from fastapi import FastAPI

from app.core.config.config import settings
from app.modules.Auth.router import oauth, oauth2

app = FastAPI(
    title="FastApI Boiler Plate Code",
    description="A ready to go boiler plate code including auth, jobs and services",
    version="1.0.0") 

app.include_router(oauth.router)
app.include_router(oauth2.router)

@app.get("/")
async def root():
    return {"Message" : "Welcome To fastapi"}
