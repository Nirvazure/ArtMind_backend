import os
from app import app

basedir=os.path.abspath(os.path.dirname(__file__))      #配置基地址
UPLOAD_FOLDER='upload'                                  #配置上传文件存储位置
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS=set(['png','jpg','JPG','PNG','gif','GIF'])   #限制上传图像文件格式