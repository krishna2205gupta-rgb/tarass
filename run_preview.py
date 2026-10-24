#!/usr/bin/env python3
import os
import uvicorn

APP = "app.main:app"
APP_DIR = os.path.join(os.path.dirname(__file__), "TARA-main", "backend")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

if __name__ == "__main__":
    uvicorn.run(APP, app_dir=APP_DIR, host=HOST, port=PORT, reload=False)
