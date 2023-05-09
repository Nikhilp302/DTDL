import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from aifc import Error
from flask import jsonify, json, request
from app import app
import re
# from mysql.connector import Error
from config import *
from flask_cors import CORS
from datetime import date
import os
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
import math
import random
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity)
jwt = JWTManager()


class Login_model():
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

    def register(self, param):
        user_registered = date.today()
        user_nicename = request.json.get('user_nicename', None)
        user_login = request.json.get('user_login', None)
        display_name = request.json.get('display_name', None)
        user_pass = request.json.get('user_pass', None)
        user_url = request.json.get('https://kaas.tdtl.world', None)
        C_password = request.json.get('C_Password', None)
        user_email = request.json.get('user_email', None)
        OTP = request.json.get('OTP', None)
        h = hashlib.md5(user_pass.encode())       
        password = h.hexdigest()
        print ("Password : " +password)     
        
        if len(user_nicename) < 3 or len(user_nicename) > 20:
            return jsonify({'message': 'Invalid username. Username must be more than 3 or less than 20 digit'}), 400

    #  Verify that the Password is not less than 3 and greater than 20
        if len(user_pass) < 6 or len(user_pass) > 100:
            return jsonify({'message': 'Invalid password. Password must be more than 8 or less than 100 digit'}), 400

        self.cursor.execute(
            f"select user_login from wp_users where user_login ='{param['user_login']}'")
        result = self.cursor.fetchall()
        if len(result) > 0:
            return jsonify({'message': 'User already exists'}), 400
        else:
            # Insert user data into the database
            self.cursor.execute(
                f"INSERT INTO wp_users (user_nicename, user_login,user_email, display_name, user_pass, OTP,user_registered,user_url) VALUES ('{param['user_nicename']}', '{param['user_login']}', '{param['user_email']}', '{param['display_name']}','{password }','{param['OTP']}','{param['user_registered']}','{param['user_url']}')"),
        # access_token = create_access_token(identity=user_pass)
   # return jsonify({'Registration Successful..!!!  access_token': access_token}), 201
        return jsonify({
            "Data": result,
            'Registration Successful..!!!  access_token': result
        })

    def user_login(self, param):
     # Get the username and password from the request
        user_login = request.json.get('user_login', None)
        user_pass = request.json.get('user_pass', None)
    # Connect to the MySQL database
    # Verify that the username and password are correct

        if not all([user_login]):
            return jsonify({'message': 'Please Fill Email field'}), 400
        if not all([user_pass]):
            return jsonify({'message': 'Please Fill Password field'}), 400
        h = hashlib.md5(user_pass.encode())       
        password = h.hexdigest()
        print ("Password : " +password) 
        self.cursor.execute(
            f"SELECT * FROM wp_users WHERE user_login='{param['user_login']}' AND user_pass='{password}'")
        result = self.cursor.fetchone()
        if result is None:
            return jsonify({'message': 'Wrong username or password'}), 401
    # Create the access token
        access_token = create_access_token(identity=user_login)
        return jsonify({
            'result': result,
            'access_token': access_token,

        })

    def ActivateuserAccount(self, param):

        OTP = request.json.get('OTP', None)
    # OTP = request.json.get('OTP', None)
        self.cursor.execute(
            f"select * from wp_users where OTP ='{param['OTP']}'")
        result = self.cursor.fetchone()

        if result is None:
            return jsonify({'message': 'Wrong OTP'}), 401
        else:
            return jsonify({
                # 'access_token': access_token,
                'result': result
                # 'email': result[1],
                # 'Username': result[3],
                # # 'Contact': result[3],
                # 'User_id': result[0],
            }), 200


# function to generate OTP


    def generateOTP(self):

        # Declare a digits variable
        # which stores all digits
        digits = "0123456789"
        OTP = ""

   # length of password can be changed
   # by changing value in range
        for i in range(6):
            OTP += digits[math.floor(random.random() * 10)]
    # return "OTP is :"+OTP
        return jsonify({
            "OTP": OTP
        })


def Google_Register(self, param):
    # Get the data from the request
    user_nicename = request.json.get('user_nicename', None)
    user_login = request.json.get('user_login', None)
    display_name = request.json.get('display_name', None)
    user_pass = request.json.get('user_pass', None)
    user_email = request.json.get('user_email', None)
    try:

        # Check if user already exists
        self.cursor.execute(
            f"SELECT * FROM wp_users WHERE user_login = '{param['user_login']}'")
        result = self.cursor.fetchone()
        if result:
            return jsonify({'message': 'User already exists', 'result': result}), 400
        else:
            # Insert user data into the database
            self.cursor.execute(
                f"INSERT INTO wp_users (user_nicename, user_login,user_email, display_name, user_pass, OTP) VALUES ('{param['user_nicename']}', '{param['user_login']}', '{param['user_email']}', '{param['display_name']}', '{param['user_pass']}','{param['OTP']}')")
    except Error as e:
        return jsonify({'message': e}), 500

    return jsonify({
        "Data": result,
        'Registration Successful..!!!  access_token': result
    })
