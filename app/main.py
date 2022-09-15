from fastapi import FastAPI

from .service.movie.routers import movie
from .service.weather.routers import weather

app = FastAPI()
app.include_router(movie.router)
app.include_router(weather.router)
