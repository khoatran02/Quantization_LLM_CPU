# Model-related utilities
from llama_cpp import Llama
from .constants import DEFAULT_THREADS, DEFAULT_BATCH_SIZE, DEFAULT_CONTEXT_SIZE
import json

def create_optimized_llama(model_path: str, threads: int = DEFAULT_THREADS) -> Llama:
    """Create an optimized Llama instance for inference"""
    return Llama(
        model_path=model_path,
        n_ctx=DEFAULT_CONTEXT_SIZE,
        n_batch=DEFAULT_BATCH_SIZE,
        n_threads=threads,
        n_gpu_layers=0,     # CPU-only
        use_mlock=True,     # Lock memory to prevent swapping
        use_mmap=True,      # Use memory mapping for faster loading
        verbose=False
    )
    
def create_financial_prompt(company_data) -> str:
    """Create a financial analysis prompt from company data"""
    base_prompt = """
    Bạn là một chuyên gia phân tích đầu tư cao cấp tại một quỹ đầu tư lớn. 
    Nhiệm vụ của bạn là xem xét các kết quả định lượng và viết một báo cáo tổng hợp súc tích, chuyên nghiệp.

    DỮ LIỆU CÔNG TY:
    {company_data}

    YÊU CẦU:
    1. Tổng hợp và viết lại thành một bản nhận định chuyên nghiệp
    2. Đưa ra mức định giá hợp lý và nhận định
    3. Đề xuất chiến lược đầu tư trong 6 tháng tới

    Văn phong chuyên nghiệp, tự tin và tập trung vào kết quả.
    """
    return base_prompt.format(company_data=json.dumps(company_data, indent=2, ensure_ascii=False))