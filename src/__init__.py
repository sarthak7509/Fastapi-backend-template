"""
Application configuration holder
Version: 1.0
Author
    Sarthak Bhatnagar
"""
import sys
from fastapi import FastAPI
from .core import logger

app = FastAPI()

# Add routers

# Export the app
__all__ = [
    app
]