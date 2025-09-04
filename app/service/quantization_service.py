# Service for model quantization
import os
from huggingface_hub import snapshot_download
from common.helpers import run_command, ensure_directory_exists
from common.constants import HF_MODEL_ID, MODEL_DIR, QUANT_4BIT, QUANT_8BIT

class QuantizationService:
    """Service for handling model quantization"""
    
    def __init__(self):
        self.llama_cpp_dir = "llama.cpp"
        self.quantized_dir = MODEL_DIR
    
    def download_model(self) -> bool:
        """Download the model from Hugging Face Hub"""
        try:
            print(f"Downloading model {HF_MODEL_ID}...")
            snapshot_download(
                repo_id=HF_MODEL_ID, 
                local_dir=f"{HF_MODEL_ID}", 
                revision="main"
            )
            return True
        except Exception as e:
            print(f"Error downloading model: {e}")
            return False
    
    def build_llama_cpp(self) -> bool:
        """Build llama.cpp from source"""
        print("Building llama.cpp...")
        
        # Create build directory and build
        if not run_command(["cmake", "-B", "build"], self.llama_cpp_dir):
            return False
        
        if not run_command(["cmake", "--build", "build", "--config", "Release"], self.llama_cpp_dir):
            return False
            
        return True
    
    def convert_to_gguf(self) -> bool:
        """Convert HF model to GGUF format"""
        print("Converting model to GGUF format...")
        
        cmd = [
            "python", "convert_hf_to_gguf.py", 
            f"../{HF_MODEL_ID}", 
            "--outtype", "f16", 
            "--outfile", f"../{MODEL_DIR}/Qwen3-8B_FP16.gguf"
        ]
        
        return run_command(cmd, self.llama_cpp_dir)
    
    def quantize_model(self, quantization_type: str) -> bool:
        """Quantize model to specified format"""
        print(f"Quantizing model to {quantization_type}...")
        
        input_path = f"../{MODEL_DIR}/Qwen3-8B_FP16.gguf"
        
        if quantization_type == QUANT_4BIT:
            output_path = f"../{MODEL_DIR}/4bit/Qwen3-8B_FP16_Q4_K_M.gguf"
        elif quantization_type == QUANT_8BIT:
            output_path = f"../{MODEL_DIR}/8bit/Qwen3-8B_FP16_Q8_0.gguf"
        else:
            raise ValueError(f"Unsupported quantization type: {quantization_type}")
        
        # Ensure output directory exists
        ensure_directory_exists(os.path.dirname(output_path))
        
        cmd = [
            "build/bin/llama-quantize", 
            input_path, 
            output_path, 
            quantization_type
        ]
        
        return run_command(cmd, self.llama_cpp_dir)
    
    def setup_models(self) -> bool:
        """Complete setup process for both 4-bit and 8-bit models"""
        # Create directories
        ensure_directory_exists(self.quantized_dir)
        ensure_directory_exists(f"{self.quantized_dir}/4bit")
        ensure_directory_exists(f"{self.quantized_dir}/8bit")
        
        # Download model
        if not self.download_model():
            return False
        
        # Build llama.cpp
        if not self.build_llama_cpp():
            return False
        
        # Convert to GGUF
        if not self.convert_to_gguf():
            return False
        
        # Quantize to 4-bit
        if not self.quantize_model(QUANT_4BIT):
            return False
        
        # Quantize to 8-bit
        if not self.quantize_model(QUANT_8BIT):
            return False
        
        print("Model setup completed successfully!")
        return True