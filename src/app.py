from fastapi import FastAPI
from src.routes.router import router

app = FastAPI(docs_url="/docs", title="PatPet gerenciamento de clinica veterinária", version="0.1")
app.include_router(router)
