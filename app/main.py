from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.liblouis import router as LIBLOUIS_ROUTES

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(LIBLOUIS_ROUTES)