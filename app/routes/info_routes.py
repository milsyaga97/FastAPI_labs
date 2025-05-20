from fastapi import APIRouter, Request
import os
from sqlalchemy import text
from app.database.database import session_dep
from app.schema.info import ServerInfo, ClientInfo, DatabaseInfo

info_router = APIRouter(prefix="/info", tags=["Info"])

@router.get("/server", response_model=ServerInfo)
async def get_server_info():
    return ServerInfo(
        python_version=os.popen("python --version").read().strip(),
        server_software="FastAPI + Uvicorn"
    )

@router.get("/client", response_model=ClientInfo)
async def get_client_info(request: Request):
    return ClientInfo(
        ip=request.client.host,
        user_agent=request.headers.get("user-agent")
    )

@router.get("/database", response_model=DatabaseInfo)
async def get_database_info(session: session_dep):
    info = session.query(text('version()')).scalar()
    return DatabaseInfo(info=info)