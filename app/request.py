from service.quantization_service import QuantizationService
import requests
import json


quant_service = QuantizationService()
quant_service.setup_models()


data = {
    "company_data": {
        "name": "Công ty ABC",
        "revenue": 1000000000000,
        "profit": 150000000000,
        "assets": 5000000000000
    }
}

response = requests.post(
    "http://localhost:8000/api/v1/analyze",
    json={
        "json_input": json.dumps(data),
        "model_type": "4bit"
    }
)

print(response.json())