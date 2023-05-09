from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
from flask_jwt_extended import JWTManager

jwt = JWTManager()

CORS(app)

@app.route("/")
def welcome():
    return jsonify({
        "Message":"Welcome to KAAS Project"
    }),200

# import controller.user_controller as user_controller
# import controller.product_controller as product_controller
# or we can write in a single line like below as well
# from controller import user_controller, product_controller
# OR
from Controller import *
from Model import *

app.secret_key = 'ChangeMe!'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)