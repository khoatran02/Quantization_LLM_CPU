# Constants used throughout the application

# Model paths
MODEL_DIR = "llm_models"
MODEL_4BIT_PATH = f"{MODEL_DIR}/4bit/Qwen3-8B_FP16_Q4_K_M.gguf"
MODEL_8BIT_PATH = f"{MODEL_DIR}/8bit/Qwen3-8B_FP16_Q8_0.gguf"
HF_MODEL_ID = "Qwen/Qwen3-8B"

# API constants
DEFAULT_MAX_TOKENS = 5000
DEFAULT_TEMPERATURE = 0.2
DEFAULT_TOP_P = 0.9

# Performance constants
DEFAULT_THREADS = 48
DEFAULT_BATCH_SIZE = 512
DEFAULT_CONTEXT_SIZE = 4096

# Quantization types
QUANT_4BIT = "Q4_K_M"
QUANT_8BIT = "Q8_0"