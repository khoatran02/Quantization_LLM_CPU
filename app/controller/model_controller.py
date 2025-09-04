# API controller for FastAPI endpoints
from flask_restx import Namespace, Resource, fields
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from service.model_service import ModelService
from common.response_common import ResponseCommon
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create namespace
model_ns = Namespace('model', description='Model-related operations')
upload_parser = model_ns.parser()
upload_parser.add_argument('json_input', type=str, required=True, help='JSON input for analysis')
upload_parser.add_argument('model_type', type=str, default="4bit", help='Model type to use')
upload_parser.add_argument('max_tokens', type=int, default=500, help='Maximum tokens for response')

response_model = model_ns.model('Response', {
    'success': fields.Boolean,
    'message': fields.String,
    'response': fields.Raw,
    'code': fields.Integer
})

# Initialize model service
model_service = ModelService()

class AnalysisRequest(BaseModel):
    json_input: str
    model_type: Optional[str] = "4bit"
    max_tokens: Optional[int] = 500

@model_ns.route("/generate_response")
class GenerateResponse(Resource):
    @model_ns.expect(upload_parser)
    @model_ns.marshal_with(response_model)
    def post(self):
        """Generate a response using the LLM"""
        try:
            args = upload_parser.parse_args()
            result = model_service.generate_response(
                args['json_input'],
                args['model_type'] if args['model_type'] is not None else "4bit",
                args['max_tokens'] if args['max_tokens'] is not None else 500
            )
            
            # FIX: Changed 'response' to 'result' and use proper structure
            return ResponseCommon(
                code=200,
                success=True,
                message="Response generated successfully",
                data=result,  # This should be the result from generate_response
            ).to_json()

        except Exception as e:
            return ResponseCommon(
                code=500,
                success=False,
                message=str(e),
                data={}
            ).to_json()

# @model_ns.route("/generate_response")
# class GenerateResponse(Resource):
#     @model_ns.expect(upload_parser)
#     @model_ns.marshal_with(response_model)

#     def post(self):
#         """Generate a response using the LLM"""

#         request = model_ns.payload
#         try:
#             result = model_service.generate_response(
#                 request.json_input,
#                 request.model_type if request.model_type is not None else "4bit",
#             request.max_tokens if request.max_tokens is not None else 500
#         )
#             return ResponseCommon(
#                 code=200,
#                 success=True,
#                 message=result,
#                 data=response,
#             ).to_json()

#         except Exception as e:
#             raise ResponseCommon(
#                 code=500,
#                 success=False,
#                 message=str(e),
#                 data={}
#             ).to_json()

@model_ns.route("/health")
class HealthCheck(Resource):
    def get(self, model_type: str = "4bit"):
        """Health check endpoint"""
        model_info = model_service.get_model_info(model_type)
        return model_info
    