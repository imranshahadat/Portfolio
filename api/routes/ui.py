"""Serves the chat user interface."""
from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["ui"])

UI_FILE = Path(__file__).resolve().parent.parent.parent / "static" / "index.html"


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def chat_ui() -> HTMLResponse:
    return HTMLResponse(UI_FILE.read_text(encoding="utf-8"))
