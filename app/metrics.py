# System metrics logic

from datetime import datetime, timezone
import os
import psutil

from .config import STARTUP_TIME

# Memory request count
REQUEST_COUNT = 0

def increment_request_count() -> None:
    global REQUEST_COUNT
    REQUEST_COUNT += 1

def get_request_count() -> int:
    return REQUEST_COUNT

def get_uptime_seconds() -> int:
    now = datetime.now(timezone.utc)
    delta = now - STARTUP_TIME
    return int(delta.total_seconds())

# Metrics from the system
def get_system_metrics() -> dict:
    # CPU
    cpu_percent = psutil.cpu_percent(interval=0.1)
    cpu_cores = psutil.cpu_count(logical=True)

    # Memory
    virtual_mem = psutil.virtual_memory()
    memory_total_mb = round(virtual_mem.total / (1024 * 1024), 2)
    memory_used_mb = round(virtual_mem.used / (1024 * 1024), 2)
    memory_percent = virtual_mem.percent

    # Disk (root partition)
    disk_usage = psutil.disk_usage(os.path.sep)
    disk_total_gb = round(disk_usage.total / (1024 * 1024 * 1024), 2)
    disk_used_gb = round(disk_usage.used / (1024 * 1024 * 1024), 2)
    disk_percent = disk_usage.percent

    # Load average (Unix based system)
    try:
        load1, load5, load15 = psutil.getloadavg()
    except (AttributeError, OSError):
        load1 = load5 = load15 = None

    return {
        "cpu": {
            "percent": cpu_percent,
            "cores": cpu_cores,
        },
        "memory": {
            "total_mb": memory_total_mb,
            "used_mb": memory_used_mb,
            "percent": memory_percent,
        },
        "disk": {
            "total_gb": disk_total_gb,
            "used_gb": disk_used_gb,
            "percent": disk_percent,
        },
        "load_average": {
            "1m": load1,
            "5m": load5,
            "15m": load15,
        },
    }

# Metris from the app
def get_app_metrics() -> dict:
    return {
        "uptime_seconds": get_uptime_seconds(),
        "requests_count": get_request_count(),
        "startup_time": STARTUP_TIME.isoformat() + "Z",
    }