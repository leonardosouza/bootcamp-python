import logging

from fastapi import FastAPI
from routers import auth_routes, item_routes

app = FastAPI()

logging.getLogger("passlib").setLevel(logging.ERROR)

# Incluindo as rotas separadas
app.include_router(auth_routes.router)
app.include_router(item_routes.router)
