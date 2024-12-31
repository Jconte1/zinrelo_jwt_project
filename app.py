import os
import time
import jwt  # PyJWT
from flask import Flask, jsonify
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()

ZINRELO_API_KEY = os.getenv("ZINRELO_API_KEY")
ZINRELO_PARTNER_ID = os.getenv("ZINRELO_PARTNER_ID")
ZINRELO_API_KEY_IDENTIFIER = os.getenv("ZINRELO_API_KEY_IDENTIFIER")

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Zinrelo!"

@app.route('/zinrelo/jwt', methods=['GET'])
def generate_zinrelo_jwt():
    """
    Returns a JWT with user data. 
    In a real scenario, you'd authenticate the user, 
    then fill out user_info with their details dynamically.
    """
    
    # Example user info
    user_info = {
        'sub': ZINRELO_API_KEY_IDENTIFIER,  # Only required if not using default key
        'member_id': 'Unique-UserID',
        'email_address': 'user@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'exp': int(time.time()) + 1800  # Expires in 30 minutes
    }
    
    encoded_jwt = jwt.encode(user_info, ZINRELO_API_KEY, algorithm='HS256')
    return jsonify({'jwt_token': encoded_jwt})

if __name__ == '__main__':
    app.run(debug=True)
