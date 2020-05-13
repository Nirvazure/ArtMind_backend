from app import app
from flask import request,jsonify,send_from_directory,make_response
from werkzeug.utils import secure_filename  #这个需要研究一下
from config import basedir,ALLOWED_EXTENSIONS
import os

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
file_dir=os.path.join(basedir,app.config['UPLOAD_FOLDER'])
# rsplit参数的第2个1，指的是分割一次
def allow_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

# strict_slashes=None,对URL最后的 / 符号是否严格要求，
@app.route('/up_photo',methods=['POST'],strict_slashes=False)
def craftupload():
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f=request.files['photo']
    if f and allow_file(f.filename):
        fname=secure_filename(f.filename)
        ext=fname.rsplit('.',1)[1]  
        new_filename = 's222' + '.' + ext  
        print(fname,ext,new_filename)
        f.save(os.path.join(file_dir,fname))
        return jsonify({"success":0,"msg":"上传成功"})
    else:
        return jsonify({{"error":1001,"msg":"上传失败"}})

@app.route('/download/<string:filename>',methods=['GET'])
def download(filename):
    if request.method=='GET':
        if os.path.isfile(os.path.join(file_dir,filename)):
            return send_from_directory(file_dir,filename,as_attachment=True)
        pass

@app.route('/show/<string:filename>',methods=['GET'])
def show_photo(filename):
    if request.method=='GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass
