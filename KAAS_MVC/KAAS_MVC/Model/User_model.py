import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from aifc import Error
from flask import jsonify, request
from app import app
# from mysql.connector import Error
from config import *
from flask_cors import CORS
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity)
jwt = JWTManager()

class User_model():
    email_regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
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

    def user_register(self, param):
        user_registered = date.today()
        user_name = request.json.get('user_name', None)
        first_name = request.json.get('first_name', None)
        last_name = request.json.get('last_name', None)
        password = request.json.get('password', None)
        is_staff = request.json.get('is_staff', None)
        is_active = request.json.get('is_active', None)
        last_login = request.json.get('last_login', None)
        is_student = request.json.get('is_student', None)
        is_lecturer = request.json.get('is_lecturer', None)
        phone = request.json.get('phone', None)
        address = request.json.get('address', None)
        email = request.json.get('email', None)
        is_parent = request.json.get('is_parent', None)
        created_date = user_registered

        OTP = request.json.get('OTP', None)
        h = hashlib.md5(password.encode())       
        Ency_password = h.hexdigest()
        print ("Password : " +password)     
        
        if len(user_name) < 3 or len(user_name) > 20:
            return jsonify({'message': 'Invalid username. Username must be more than 3 or less than 20 digit'}), 400

    #  Verify that the Password is not less than 3 and greater than 20
        if len(password) < 6 or len(password) > 100:
            return jsonify({'message': 'Invalid password. Password must be more than 8 or less than 100 digit'}), 400

        self.cursor.execute(f"select email from users where email ='{param['email']}'")
        result = self.cursor.fetchall()
        if len(result) > 0:
            return jsonify({'message': 'User already exists'}), 400
        else:
            # Insert user data into the database
            self.cursor.execute(
                f"INSERT INTO users (user_name, first_name,last_name, password, is_staff, is_active,last_login,is_student,is_lecturer,phone,address,email,is_parent,created_date) VALUES ('{param['user_name']}', '{param['first_name']}', '{param['last_name']}','{Ency_password}','{param['is_staff']}','{param['is_active']}','{param['last_login']}','{param['is_student']}','{param['is_lecturer']}','{param['phone']}','{param['address']}','{param['email']}','{param['is_parent']}','{param['created_date']}')"),
        # access_token = create_access_token(identity=user_pass)
   # return jsonify({'Registration Successful..!!!  access_token': access_token}), 201
        return jsonify({
            "Data": result,
            'Registration Successful..!!!  access_token': result
        })
    

    # region ---------------- All Courses------------------------

    def get_CourseDetails(self):
        # Query Execution code
        #self.cursor.execute(f"SELECT * FROM wp_posts")
        self.cursor.callproc('proc_my_courses', [13, ])
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