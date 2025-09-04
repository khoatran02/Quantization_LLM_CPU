import os
from flask import Flask
from flask_restx import Api
from controller.model_controller import model_ns
from service.model_service import ModelService

def create_app():
    app = Flask(__name__)

    # Initialize the API with Swagger UI at '/'
    api = Api(
        app,
        version='1.0',
        title='Document Model API',
        description='API for document model operations'
    )

    # Register namespace
    api.add_namespace(model_ns, path='/model')

    return app
  
if __name__ == '__main__':
    app = create_app()
    # IMPORTANT: bind to 0.0.0.0 and match port 8000 for Docker mapping
    app.run(host='0.0.0.0', port=8000, debug=True, use_reloader=False)
  
# if __name__ == '__main__':
#     app = create_app()
#     port = int(os.environ.get('PORT', 5000))
#     host = os.environ.get('HOST', '127.0.0.1')
#     app.run(debug=True, host=host, port=port)
