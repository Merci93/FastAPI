import logging
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from src import configurations, logger_handler


logger_handler.init_logging()
logger = logging.getLogger(__name__)

description = """
A test endpoint for FastAPI.
Developed by David Asogwa.
[Source Code](https://github.com/Merci93/FastAPI)
"""


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, Any]:
    configurations.init_settings()
    yield


app = FastAPI(
    title="FastAPI Test Endpoints",
    docs_url="/",
    description=description,
    version="0.1",
    contact={
        "name": "Developer",
        "contact": "https://github.com/Merci93/FastAPI"
    },
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/root")
def get_root() -> dict[str, str]:
    return {"message": "Hi! root api up and running."}


@app.get("/test_user/1")
def get_username(query: str) -> dict[str, str]:
    return {"message": f"Hello {query}!!! Welcome to my API endpoint."}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
