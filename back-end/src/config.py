# config.py
from flask import Flask, jsonify

class developmentConfig:
    DEBUG = True
    class SQLConfig:
        HOST = 'localhost'
        PORT = 3306
        USER = 'root'
        PASSWORD = ''
        DATABASE = 'tuprofe'
    
