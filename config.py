import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/biometria'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    SECRET_KEY = os.urandom(24)
