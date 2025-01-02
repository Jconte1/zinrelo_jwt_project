import os
import time
import jwt
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

ZINRELO_API_KEY = os.getenv("ZINRELO_API_KEY")
ZINRELO_PARTNER_ID = os.getenv("ZINRELO_PARTNER_ID")
ZINRELO_API_KEY_IDENTIFIER = os.getenv("ZINRELO_API_KEY_IDENTIFIER")

app = Flask(__name__)

# Enable CORS for specific origin(s) or all (*).
# If you trust only your domain, do:
CORS(app, resources={r"/zinrelo/*": {"origins": ["https://mld.com"]}})

@app.route('/')
def index():
    return "Hello, Zinrelo!"

@app.route('/zinrelo/jwt', methods=['GET'])
def generate_zinrelo_jwt():
    user_info = {
        'sub': ZINRELO_API_KEY_IDENTIFIER,
        'member_id': 'Unique-UserID',
        'email_address': 'user@example.com',
        'exp': int(time.time()) + 1800
    }
    encoded_jwt = jwt.encode(user_info, ZINRELO_API_KEY, algorithm='HS256')
    return jsonify({
        'jwt_token': encoded_jwt,
        'partner_id': ZINRELO_PARTNER_ID
    })

if __name__ == '__main__':
    app.run(debug=True)
