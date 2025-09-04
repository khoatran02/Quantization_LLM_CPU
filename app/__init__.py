"""
Vietnamese LLM Quantization Project

A FastAPI-based application for running quantized Vietnamese language models
with 4-bit and 8-bit quantization for financial analysis.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "Multilingual LLM with Vietnamese support for CPU inference"

# Import key components for easier access
from app.controller.model_controller import router as api_router
from app.service.model_service import ModelService
from app.service.quantization_service import QuantizationService

__all__ = [
    'api_router',
    'ModelService',
    'QuantizationService'
]