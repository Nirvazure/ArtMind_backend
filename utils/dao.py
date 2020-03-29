# encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Painter(db.Model):
    __tablename__ = 'painter'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.Image, nullable=False)


db.create_all()  # 创建数据表


@app.route('/painter[id:Integer]' method=['POST', 'PUT', 'GET', 'DELETE'])
class PainterAPI(Resource):
    def post(self):     # 增加
        painter = Painter(name='Leonard Da Vicci', content='bbb')
        db.session.add(painter)
        db.session.commit()
    def
    # 查询
    result = Painter.query.filter(Painter.name='Leonard Da Vicci').first()

    # 修改
    painter = Painter.query.filter(Painter.name='Leonard Da Vicci').first()
    painter.name = 'Van Goah'
    db.session.commit()

    def delete():       # 删除
        painter = Painter.query.filter(Painter.name='Leonard Da Vicci').first()
        db.session.delete(painter)
        db.session.commit()

