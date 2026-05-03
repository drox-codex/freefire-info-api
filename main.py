from flask import Flask, request, jsonify
import requests
import time
from utils.aes import decrypt_response
from utils.proto import parse_player_data

app = Flask(__name__)

# Configuration
API_URL = "https://client.ind.freefiremobile.com/"
TOKEN_CACHE = {"access_token": None, "expires_at": 0}

def get_valid_token():
    """Lazy-loading token refresh logic"""
    current_time = time.time()
    if TOKEN_CACHE["access_token"] is None or current_time > TOKEN_CACHE["expires_at"]:
        # In a real scenario, perform login request here
        # For this boilerplate, we simulate a token update
        TOKEN_CACHE["access_token"] = "dummy_session_token_12345"
        TOKEN_CACHE["expires_at"] = current_time + 3600
    return TOKEN_CACHE["access_token"]

@app.route('/api/info', methods=['GET'])
def get_player_info():
    uid = request.args.get('uid')
    region = request.args.get('region', 'IND')

    if not uid:
        return jsonify({"error": "UID parameter is required"}), 400

    token = get_valid_token()
    
    # Example request structure
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11;)",
        "X-GA": "platform=1&app_version=1.100.1",
        "Authorization": f"Bearer {token}"
    }
    
    try:
        # This is a placeholder for the actual encrypted protobuf request
        # response = requests.get(f"{API_URL}/player/{uid}", headers=headers, timeout=10)
        # decrypted_data = decrypt_response(response.content)
        # data = parse_player_data(decrypted_data)
        
        # Mocked response for structure visibility
        data = {
            "uid": uid,
            "region": region,
            "nickname": "VercelUser",
            "level": 70,
            "exp": 150400,
            "status": "Online"
        }
        
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return jsonify({
        "message": "Free Fire Info API is running on Vercel",
        "endpoint": "/api/info?uid=12345678"
    })

if __name__ == '__main__':
    app.run()