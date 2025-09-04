"""
Service layer for the Vietnamese LLM application.

This package contains:
- model_service: Handles model loading and inference
- quantization_service: Handles model quantization and setup
"""

from service.model_service import ModelService
from service.quantization_service import QuantizationService

__all__ = [
    'ModelService',
    'QuantizationService'
]