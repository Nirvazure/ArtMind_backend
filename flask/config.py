import os
from app import app

basedir=os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS=set(['png','jpg','JPG','PNG','gif','GIF'])