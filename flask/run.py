from app import app
from flask import Flask
from flask_restful import Api  # Restful API支持
from flask_cors import CORS  # 跨域支持
from app import resource  # 载入预设的API接口
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_app():
    app = Flask(__name__)  # 创建Flask服务
    CORS(app)  # 跨域配置
    api = Api(app)  # RestAPI服务配置
    api.add_resource(resource.Home, '/home')
    api.add_resource(resource.Analyse, '/analyse')
    api.add_resource(resource.Gallery, '/gallery')
    api.add_resource(resource.Index, '/')
    engine = create_engine('mysql+pymysql://root:localhost/flask')
    DBSession = sessionmaker(bind=engine)  # 数据库配置
    return app


if __name__ == '__main__':
    # app = create_app()          #创建服务
    app.run(debug=True)  # 启动服务
