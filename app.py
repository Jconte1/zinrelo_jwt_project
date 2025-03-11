from flask import Flask, jsonify, request
import os
import time
import jwt
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

ZINRELO_API_KEY = os.getenv("ZINRELO_API_KEY")
ZINRELO_PARTNER_ID = os.getenv("ZINRELO_PARTNER_ID")
ZINRELO_API_KEY_IDENTIFIER = os.getenv("ZINRELO_API_KEY_IDENTIFIER")

app = Flask(__name__)

# Enable CORS for specific origin(s) or all (*).
CORS(app, resources={r"/zinrelo/*": {"origins": ["https://shop.mld.com"]}})

@app.route('/')
def index():
    return "Hello, Zinrelo!"

@app.route('/zinrelo/jwt', methods=['GET'])
def generate_zinrelo_jwt():
   
    email_address = request.args.get('email_address', '') or 'example@test.com' 

    
    if not email_address:
        return jsonify({'error': 'Missing email_address (required as member_id)'}), 400

    user_info = {
        'sub': ZINRELO_API_KEY_IDENTIFIER,
        'member_id': email_address,  
        'email_address': email_address,
        'exp': int(time.time()) + 1800  # Token expires in 30 minutes
    }

    encoded_jwt = jwt.encode(user_info, ZINRELO_API_KEY, algorithm='HS256')
    return jsonify({
        'jwt_token': encoded_jwt,
        'partner_id': ZINRELO_PARTNER_ID
    })

if __name__ == '__main__':
    app.run(debug=True)
