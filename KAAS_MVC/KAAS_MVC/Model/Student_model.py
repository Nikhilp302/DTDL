from flask import jsonify, json, request
from app import app
import re
from config import *
from flask_cors import CORS
# import pandas as pd
import os
import bcrypt
import math
import random
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity)


class Student_model():
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

    def get_Student_profile(self, param):
        self.cursor.execute(
            f"SELECT * FROM wp_users where ID ='{param['ID']}'")
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

    # Get Course By Id
    def getNumberOfStudent(self, param):
        # cursor = connection.cursor(dictionary=True)
        self.cursor.execute(
            f"SELECT * FROM student_certificate WHERE course_id ='{param['course_id']}'")
        # SELECT * FROM wp_users WHERE ID=user_id;
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
