from pydantic import BaseModel

class ServerInfo(BaseModel):
    python_version: str
    server_software: str

class ClientInfo(BaseModel):
    ip: str
    user_agent: str

class DatabaseInfo(BaseModel):
    info: str