"""
Controller layer for the Vietnamese LLM API.

This package contains:
- api_controller: FastAPI routes for model inference and management
"""

from controller.model_controller import model_ns

__all__ = [
    'model_ns'
]