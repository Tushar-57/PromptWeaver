from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from llm_service import process_user_request

app = Flask(__name__)
CORS(app, resources={
    r"/generate": {
        "origins": "http://localhost:5173",
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

app.logger.setLevel(logging.DEBUG)

@app.route('/generate', methods=['POST', 'OPTIONS'])
def generate():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    try:
        data = request.get_json(force=True)
        app.logger.debug("Received request data: %s", data)
        
        # Process the request via our LLM service.
        assistant_response, log_details = process_user_request(data, app.logger)
        
        # (Optional) Log the configuration details for debugging.
        app.logger.info("Configuration Details: %s", log_details)
        
        return jsonify({
            'status': 'success',
            'assistant_response': assistant_response,
            'received_data': data
        })
        
    except Exception as e:
        app.logger.error("Error processing request: %s", str(e))
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

def _build_cors_preflight_response():
    response = jsonify({"status": "preflight"})
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
