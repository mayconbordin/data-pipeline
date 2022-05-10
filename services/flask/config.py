"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = True
    DEBUG = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SESSION_COOKIE_NAME = 'my_cookie'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://analytics:analytics@analytics-postgres:5401/analytics')
    SQLALCHEMY_USERNAME = 'analytics'
    SQLALCHEMY_PASSWORD = 'analytics'
    SQLALCHEMY_DATABASE_NAME = 'analytics'
    SQLALCHEMY_TABLE = 'migrations'
    SQLALCHEMY_DB_SCHEMA = 'public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
