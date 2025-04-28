from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

#base function
@app.route('/')
def welcome():
    print("you're inside the welocome function")
    return "Hello, welcome to JWT token"

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # # Verify credentials (simplified)
    if username == 'test' and password == 'test':
        access_token = create_access_token(identity=username)
        print(f"the access token was succesfully generated: {access_token}")
        return jsonify(access_token=access_token)
    print("in login func tetsing")
    return jsonify({"msg": "Invalid credentials"}), 401


# Protected route
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    print("in protected function testing")

    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)

    
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
           
    