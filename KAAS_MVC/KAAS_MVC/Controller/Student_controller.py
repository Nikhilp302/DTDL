from app import app
from flask import request
from Model.Student_model import Student_model
from flask_cors import CORS
CORS(app)

obj = Student_model()
@app.route("/StudentProfile",methods=["POST"])
def get_Student_profile():
    return obj.get_Student_profile(request.json)

obj = Student_model()
@app.route("/NumberOfStudent",methods=["POST"])
def getNumberOfStudent():
    return obj.getNumberOfStudent(request.json)