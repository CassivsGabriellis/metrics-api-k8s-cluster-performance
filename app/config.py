from datetime import datetime, timezone
import os

APP_NAME = "metrics-api"
APP_VERSION = "1.0.0"
APP_ENV = os.getenv("APP_ENV", "dev")

# Moment that the process started (to calculate uptime)
STARTUP_TIME =  datetime.now(timezone.utc)