from fastapi import FastAPI

from app.routes.info_routes import info_router

app = FastAPI()
app.include_router(info_router)
