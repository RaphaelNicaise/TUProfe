# config.py
from flask import Flask, jsonify

class developmentConfig:
    DEBUG = True
    SECRET_KEY = '898v0284nv5874903489vet83v0u9t983v0v3rvere'
    class SQLConfig:
        HOST = 'localhost'
        PORT = 3306
        USER = 'root'
        PASSWORD = ''
        DATABASE = 'tuprofe'
    
