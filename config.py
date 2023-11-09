import os

# This is home base for our app
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Here's the lowdown on how we set up the Flask app
class Config(object):
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'tmp')  # Where we'll store uploaded files
    ALLOWED_EXTENSIONS = {'wav'}  # Only '.wav' files are cool for us
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # Don't let uploads be more than 50MB
