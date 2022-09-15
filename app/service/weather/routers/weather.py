from typing import Optional
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

TEMPLATE_DIR = Path().resolve().joinpath("app").joinpath("templates").joinpath("weather")
templates = Jinja2Templates(directory=TEMPLATE_DIR)


@router.get("/weather", response_class=HTMLResponse)
async def read_item(request: Request, q: Optional[str] = None):
    return templates.TemplateResponse("weather.html", {"request": request, "id": q})
