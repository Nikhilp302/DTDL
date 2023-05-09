from app import app
from flask import request
from Model.Login_model import Login_model
from flask_cors import CORS
CORS(app)

obj = Login_model()

# region -------------Registration--------------
@app.route("/register", methods=["POST"])
def register():
    return obj.register(request.json) 
# endregion ---------------------------------------

@app.route("/user_login",methods=["POST"])
def user_login():
    return obj.user_login(request.json)
#end-----------------------------------------

# Activate User
@app.route("/ActivateuserAccount",methods=["POST"])
def ActivateuserAccount():
    return obj.ActivateuserAccount(request.json)
#end Activate user

#Generate OTP
@app.route("/generateOTP",methods=["GET"])
def generateOTP():
    return obj.generateOTP()
#end OTP
# @app.route('/Google_Register', methods=['POST'])
def Google_Register():
    return obj.Google_Register(request.json)