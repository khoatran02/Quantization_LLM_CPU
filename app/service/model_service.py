# Service for model inference
import os
import time
import json
from typing import Dict, Any, Optional, Tuple
from llama_cpp import Llama
from common.model_utils import create_optimized_llama, create_financial_prompt
from common.constants import MODEL_4BIT_PATH, MODEL_8BIT_PATH
from common.helpers import validate_json_input
from common.response_common import ResponseCommon

class ModelService:
    """Service for handling model inference"""
    
    def __init__(self):
        # Use Optional[Llama] for type hinting
        self.models: Dict[str, Llama | None] = {
            "4bit": None,
            "8bit": None
        }

    def load_model(self, model_type: str = "4bit") -> str:
        """Load the specified model into memory"""
        try:
            if model_type == "4bit":
                model_path = MODEL_4BIT_PATH
            elif model_type == "8bit":
                model_path = MODEL_8BIT_PATH
            else:
                return f"Unsupported model type: {model_type}"
            
            if not os.path.exists(model_path):
                return f"Model file not found at path: {model_path}"

            self.models[model_type] = create_optimized_llama(model_path)
            if self.models[model_type] is not None:
                return f"Model {model_type} loaded successfully"
            else:
                return f"Failed to load model of type: {model_type}"
        except Exception as e:
            return f"Error loading model: {e}"

    def generate_response(self, json_input: str, model_type: str = "4bit", max_tokens: int = 500) -> Dict[str, Any]:
        """Generate a response based on JSON input"""
        start_time = time.time()
        
        # Validate and parse JSON input
        data_json_str = json.dumps(json_input)
        data = validate_json_input(data_json_str)
        
        # Select appropriate model
        if model_type not in self.models or self.models[model_type] is None:
            self.load_model(model_type)
        model = self.models[model_type]
        if model is None:
            raise RuntimeError(f"Model '{model_type}' is not loaded.")
        
        # Create prompt from JSON data
        prompt = create_financial_prompt(data)
        print(prompt)
        
        # Generate response
        messages = [
            {"role": "system", "content": "Bạn là một chuyên gia phân tích đầu tư cao cấp."},
            {"role": "user", "content": prompt}
        ]
        
        output = model.create_chat_completion(
            messages=messages, # type: ignore
            max_tokens=max_tokens,
            temperature=0.2,
            top_p=0.9
        )

        response = output["choices"][0]["message"]["content"] # type: ignore

        print(response)
        
        # Calculate performance metrics
        processing_time = time.time() - start_time
        token_count = len(response.split())  # type: ignore # Approximate
        
        response = {
            "response": response,
            "processing_time": round(processing_time, 2),
            "tokens_generated": token_count,
            "tokens_per_second": round(token_count / processing_time, 2) if processing_time > 0 else 0,
            "model_type": model_type
        }

        return response
        
    def get_model_info(self, model_type: str = "4bit") -> Dict[str, Any]:
        """Get information about the loaded model"""
        try:

            if model_type not in self.models or self.models[model_type] is None:
                message = self.load_model(model_type)

            if self.models[model_type] is None:
                return ResponseCommon(
                    code=404,
                    success=False,
                    message=message,
                    data={}
                ).to_json()

            response = {
                "model_path": MODEL_4BIT_PATH if model_type == "4bit" else MODEL_8BIT_PATH,
                # "context_size": self.models[model_type].n_ctx, 
                "threads": self.models[model_type].n_threads, 
                "model_type": model_type
            }
            return ResponseCommon(
                code=200,
                success=True,
                message=message,
                data=response,
            ).to_json()

        except Exception as e:
            return ResponseCommon(
                code=500,
                success=False,
                message=f"Error during model info retrieval: {str(e)}",
                data=[]
            ).to_json()
