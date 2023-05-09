from app import app
from flask import request
from Model.Course_model import Course_model
from flask_cors import CORS
CORS(app)

obj = Course_model()


@app.route("/Courses",methods=["GET"])
def getall_course_model():
    return obj.getall_course_model() 



@app.route("/Course_ById",methods=["POST"])
def getCourse_ById():
    return obj.getCourse_ById(request.json)



@app.route("/Popular_Course",methods=["GET"])
def getall_Popular_Course_model():
    return obj.getall_Popular_Course_model()

@app.route("/CoursesByUserId",methods=["POST"])
def getall_Popular_User_Course_modelList():
    return obj.getall_Popular_User_Course_modelList(request.json)



