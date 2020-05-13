class CraftTask(db.Model):
    __tablename__ = 'moment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    model = db.relationship('Model', secondary=article_tag,
                            backref=db.backref('articles'))


painter_style = db.Table('painter_style',
                         db.Column('painter_id', db.Integer, db.ForeignKey(
                             'painter_id'), primary_key=True),
                         db.Column('painter_id', db.Integer, db.ForeignKey('painter_id'), primary_key=True))


class Painter(db.Model):
    __tablename__ = 'painter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    styles = db.relationship('Style', secondary=painter_style,
                             backref=db.backref('painter'))


class Style(db.Model):
    __tablename__ = 'style'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


这里是设置多对多关系的关键地方，relationship在上篇文章中也用过。backref是反向引用。然后需要添加一个中间表，用来关联Article表和Tag表。代码如下，
