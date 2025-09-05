# Quantization LLM for CPU
## Overview

This project offers a complete framework for quantizing Large Language Models (LLMs) to enhance CPU inference efficiency. It features an API for serving quantized models, a Jupyter notebook for experimentation, and pre-quantized model examples.

### ✨ Features

- **Model Quantization:** Supports 4-bit and 8-bit quantization to reduce model size and speed up inference.
- **API Services:** Provides a robust API for serving and interacting with quantized models.
- **Dockerized Deployment:** Includes a Dockerfile for streamlined containerized deployment.
- **Modular Architecture:** Organized codebase with clear separation of controllers, services, and utilities.
- **Testing Included:** Scripts for validating API functionality.

### 📂 Project Structure

```
Quantization_LLM_CPU/
├── Quantizing_LLM.ipynb
├── app/
│   ├── __init__.py
│   ├── Dockerfile
│   ├── main.py
│   ├── request.py
│   ├── requirements.txt
│   ├── test_api.py
│   ├── common/
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── helpers.py
│   │   ├── model_utils.py
│   │   └── response_common.py
│   ├── controller/
│   │   ├── __init__.py
│   │   └── model_controller.py
│   ├── llm_models/
│   │   ├── 4bit/
│   │   │   └── Qwen3-8B_FP16_Q4_K_M.gguf
│   │   └── 8bit/
│   │       └── Qwen3-8B_FP16_Q8_0.gguf
│   └── service/
│       ├── __init__.py
│       ├── model_service.py
│       └── quantization_service.py
└── README.md
```

### 🛠️ Component Breakdown

- **Quantizing_LLM.ipynb:** Jupyter notebook for experimenting with quantization techniques and evaluating performance.
- **app/**: Main application directory.
    - **main.py:** API server entry point.
    - **request.py:** API request structures.
    - **requirements.txt:** Python dependencies.
    - **test_api.py:** API endpoint tests.
    - **Dockerfile:** Docker image build instructions.
- **common/**: Shared utilities and constants.
    - **constants.py:** Configuration values.
    - **helpers.py:** Helper functions.
    - **model_utils.py:** LLM interaction utilities.
    - **response_common.py:** Common API responses.
- **controller/**: Business logic.
    - **model_controller.py:** LLM operations management.
- **llm_models/**: Pre-quantized models.
    - **4bit/**: 4-bit models.
    - **8bit/**: 8-bit models.
- **service/**: Model management and quantization logic.
    - **model_service.py:** LLM loading and serving.
    - **quantization_service.py:** Model quantization logic.

### 🚀 Getting Started

**Prerequisites:**  
- Python 3.10+  
- pip

**Install dependencies:**
```bash
pip install -r app/requirements.txt
```

**Run the application:**
```bash
python app/main.py
```

**Test the API:**
```bash
python app/test_api.py
```

**Experiment with quantization:**
```bash
jupyter notebook Quantizing_LLM.ipynb
```

### 📜 License

Licensed under the MIT License.
