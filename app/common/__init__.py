"""
Common utilities and helpers for the Vietnamese LLM application.

This package contains:
- constants: Application-wide constants
- helpers: Utility functions for file operations, command execution, etc.
- model_utils: Model-specific utilities and prompt generation
"""

from common.constants import (
    MODEL_DIR,
    MODEL_4BIT_PATH,
    MODEL_8BIT_PATH,
    HF_MODEL_ID,
    DEFAULT_MAX_TOKENS,
    DEFAULT_TEMPERATURE,
    DEFAULT_TOP_P,
    DEFAULT_THREADS,
    DEFAULT_BATCH_SIZE,
    DEFAULT_CONTEXT_SIZE,
    QUANT_4BIT,
    QUANT_8BIT
)

from common.helpers import (
    ensure_directory_exists,
    run_command,
    validate_json_input
)

from common.model_utils import (
    create_optimized_llama,
    create_financial_prompt
)

__all__ = [
    # Constants
    'MODEL_DIR',
    'MODEL_4BIT_PATH',
    'MODEL_8BIT_PATH',
    'HF_MODEL_ID',
    'DEFAULT_MAX_TOKENS',
    'DEFAULT_TEMPERATURE',
    'DEFAULT_TOP_P',
    'DEFAULT_THREADS',
    'DEFAULT_BATCH_SIZE',
    'DEFAULT_CONTEXT_SIZE',
    'QUANT_4BIT',
    'QUANT_8BIT',
    
    # Helpers
    'ensure_directory_exists',
    'run_command',
    'validate_json_input',
    
    # Model Utilities
    'create_optimized_llama',
    'create_financial_prompt'
]