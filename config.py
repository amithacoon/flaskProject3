import os

# Base directory of the application
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Configuration settings for the Flask application
class Config(object):
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'tmp')
    ALLOWED_EXTENSIONS = {'wav'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB upload limit

