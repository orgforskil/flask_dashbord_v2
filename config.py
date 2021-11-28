import os
from pathlib import Path

ROOT = Path().parent.resolve()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'THIS_is_a_Secret_key_1123456_@#$%^&*('

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(ROOT / 'db' / 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
