import threading
import time
import logging
from flask import Flask, jsonify, request
from config import Config
from utils.crypto import AESCipher
from utils.protobuf_handler import ProtobufHandler
import requests

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
cipher = AESCipher(Config.AES_KEY, Config.AES_IV)

# Global state for credentials to be accessed by background thread
credentials = {
    "token": Config.ACCESS_TOKEN,
    "lock": threading.Lock()
}

class TokenRefresher(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def run(self):
        logging.info("Token refresh thread started.")
        while not self._stop_event.is_set():
            try:
                # Logic to refresh token via Garena API
                logging.info("Refreshing access token...")
                # response = requests.post(Config.SERVER_URL + Config.AUTH_ENDPOINT, ...)
                
                with credentials["lock"]:
                    # credentials["token"] = response.json().get('new_token')
                    credentials["token"] = "refreshed_" + str(int(time.time()))
                
                # Sleep for interval or until stopped
                self._stop_event.wait(Config.REFRESH_INTERVAL)
            except Exception as e:
                logging.error(f"Error in token refresh: {e}")
                time.sleep(60) # Retry after 1 minute

# Initialize background thread
refresher = TokenRefresher()
refresher.start()

@app.route('/player/<player_id>', methods=['GET'])
def get_player_info(player_id):
    try:
        with credentials["lock"]:
            current_token = credentials["token"]

        # Prepare request
        params = {"uid": player_id, "access_token": current_token}
        
        # In a real scenario, requests might need encrypted payloads
        # payload = cipher.encrypt(f"uid={player_id}")
        
        response = requests.get(
            f"{Config.SERVER_URL}{Config.PLAYER_INFO_ENDPOINT}",
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            # If response is encrypted
            # decrypted_data = cipher.decrypt(response.text)
            
            # If response is Protobuf (Binary)
            # data = ProtobufHandler.decode_to_json(PlayerMessageClass, response.content)
            
            return jsonify({
                "status": "success",
                "player_id": player_id,
                "data": response.json() # Assuming JSON for demo
            })
        else:
            return jsonify({"error": "API returned error", "code": response.status_code}), response.status_code

    except Exception as e:
        logging.error(f"Request failed: {e}")
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "thread_alive": refresher.is_alive()})

if __name__ == '__main__':
    try:
        # production mode should use a proper WSGI server like Gunicorn
        app.run(host='0.0.0.0', port=5000, debug=False)
    finally:
        refresher.stop()
        refresher.join()