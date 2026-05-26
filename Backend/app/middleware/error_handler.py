# app/middleware/error_handler.py
from fastapi import Request
from fastapi.responses import JSONResponse

async def system_exception_handling_catch(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error_intercepted": "Internal System Error", "technical_detail": str(exc)}
    )