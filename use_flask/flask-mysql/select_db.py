#!/usr/bin/env python
# -*- coding=utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_, not_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:adbibo@localhost/flask'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    phone = db.Column(db.String(32), nullable=False)

    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone

    def __repr__(self):
        return "<User'{:s}' > ".format(self.username)
        # return 'User %r' % self.username


select_ = User.query.filter_by(username='itmin').first()
print(select_.id)  # 精确查询，并查找出ID

print User.query.filter(User.email.endswith('@qq.com')).all()  # 模糊查询

print User.query.filter(User.phone.endswith('13812345678')).all()

print User.query.filter(User.username != 'yoyo').first()  # 反条件查询，非

print User.query.filter(not_(User.username == 'yoyo')).first()

print User.query.filter(or_(User.username != 'yoyo', User.email.endswith('@example.com'))).first()  # 或查询
print User.query.filter(and_(User.username != 'yoyo', User.email.endswith('@example.com'))).first()  # 与查询
print User.query.limit(10).all()  # 查询返回的数据的数目

data_all = User.query.all()
print (data_all)  # 查询全部

for i in range(len(data_all)):
    print data_all[i].username + " " + data_all[i].email + " " + data_all[i].phone
