import os

class Config:
    # API Configuration
    SERVER_URL = "https://freefire.api.garena.com" # Placeholder
    AUTH_ENDPOINT = "/api/v1/login"
    PLAYER_INFO_ENDPOINT = "/api/v1/player_info"

    # Security Keys (Must be 16, 24, or 32 bytes for AES)
    AES_KEY = os.getenv("FF_AES_KEY", "this_is_a_secret_key_32_bytes_len")
    AES_IV = os.getenv("FF_AES_IV", "this_is_an_iv_16")

    # Credentials
    ACCOUNT_ID = os.getenv("FF_ACCOUNT_ID", "12345678")
    ACCESS_TOKEN = os.getenv("FF_ACCESS_TOKEN", "default_token")
    
    # Refresh Interval (seconds)
    REFRESH_INTERVAL = 3600