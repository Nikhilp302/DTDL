from app import app
from flask import request
from Model.User_model import User_model
from flask_cors import CORS
CORS(app)

obj=User_model()

# region -------------Registration--------------
@app.route("/User_registration", methods=["POST"])
def user_register():
    return obj.user_register(request.json) 
# endregion ---------------------------------------

# region -------------Registration--------------
@app.route("/Cour", methods=["GET"])
def get_CourseDetails():
    return obj.get_CourseDetails(request.json) 
# endregion ---------------------------------------