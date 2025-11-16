# FastAPI logic with the endpoints

from fastapi import FastAPI, Request
from datetime import datetime, timezone

from . import config
from .metrics import (
    get_system_metrics,
    get_app_metrics,
    increment_request_count,
)

app = FastAPI(
    title=config.APP_NAME,
    version=config.APP_VERSION,
)

# Middleware to count requests
@app.middleware("http")
async def count_requests_middleware(request: Request, call_next):
    response = None
    try:
        response = await call_next(request)
        return response
    finally:
        # Increment request count after response is sent
        increment_request_count()

@app.get("/health", tags=["Health checkpoint"])
async def health_check():
    """
    Health check endpoint.
    Useful for kubernetes liveness and readiness probes.
    """
    return {
        "status": "ok",
        "app_name": config.APP_NAME,
        "app_version": config.APP_VERSION,
        "app_env": config.APP_ENV,
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
    }

@app.get("/info", tags=["App Info"])
async def app_info():
    """
    Application information endpoint.
    """
    return {
        "app_name": config.APP_NAME,
        "app_version": config.APP_VERSION,
        "app_env": config.APP_ENV,
        "startup_time": config.STARTUP_TIME.isoformat() + "Z",
    }

@app.get("/metrics/system", tags=["System metrics"])
async def system_metrics():
    """
    Endpoint to get system metrics.
    """
    metrics = get_system_metrics()
    return metrics

@app.get("/metrics/app", tags=["Application metrics"])
async def app_metrics():
    """
    Endpoint to get application metrics.
    """
    metrics = get_app_metrics()
    return metrics