# config.py
from flask import Flask, jsonify
import os
class developmentConfig:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    class SQLConfig:
        HOST = 'localhost'
        PORT = 3306
        USER = 'root'
        PASSWORD = ''
        DATABASE = 'tuprofe'
    
