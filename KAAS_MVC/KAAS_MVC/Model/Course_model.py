from flask import jsonify, json
from app import app
from config import *
from flask_cors import CORS
# import pandas as pd
import os


class Course_model():
    CORS(app)
    # business Logic
    # Constructor code

    def __init__(self):
        # Connection Establishment code
        try:
            self.connection = psycopg2.connect(
                "postgresql://postgres:12345@localhost:5432/KAAS")
            self.cursor = self.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)
            self.connection.autocommit = True
            print("Connection Successful.....!")
        except:
            print("Some Error.....!")
# region ---------------- All Courses------------------------

    def getall_course_model(self):
        # Query Execution code
        self.cursor.execute(f"SELECT * FROM wp_posts")
        result = self.cursor.fetchall()
        if len(result) > 0:
            # return json.dumps(result)
            return jsonify({
                "Message": "Data Retrieved Success",
                "Data": result
            }), 200
        else:
            return jsonify({
                "Message": "No Data Found",
                "Data": result
            }), 200
# endregion -------------------------------------------------

# Get Course By Id
    def getCourse_ById(self, param):
        self.cursor.execute(
            f"SELECT * FROM wp_posts where ID ='{param['ID']}'")
        result = self.cursor.fetchall()
        if len(result) > 0:
            # return json.dumps(result)
            return jsonify({
                "Message": "Data Retrieved Success",
                "Data": result
            }), 200
        else:
            return jsonify({
                "Message": "No Data Found",
                "Data": result
            }), 200

        # Get Popular Course

    def getall_Popular_Course_model(self):
        self.cursor.execute(f"SELECT * FROM wp_posts limit 3")
        result = self.cursor.fetchall()
        if len(result) > 0:
            # return json.dumps(result)
            return jsonify({
                "Message": "Data Retrieved Success",
                "Data": result
            }), 200
        else:
            return jsonify({
                "Message": "No Data Found",
                "Data": result
            }), 200
        
    def getall_Popular_User_Course_modelList(self,param):
        self.cursor.execute(f"SELECT * FROM wp_users where ID ='{param['ID']}'")
        result = self.cursor.fetchone()
        userid=result['ID']
        # print(userid)
        self.cursor.execute(
            f"SELECT * FROM wp_posts where ID ='{userid}'")
        result1 = self.cursor.fetchall()
        res = jsonify({"res1":result, "res2":result1})
        if len(result) > 0:
            # return json.dumps(result)
            return jsonify({
                "Message": "Data Retrieved Success",
                "Data": res
            }), 200
        # else:
        #     return jsonify({
        #         "Message": "No Data Found",
        #         "Data": result
        #     }), 200
