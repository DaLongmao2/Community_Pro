#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime
import shortuuid as shortuuid
from APP.extension import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(150), primary_key=True, default=shortuuid.uuid)
    username = db.Column(db.String(64), default='新用户...')
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 经验
    points = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    gender = db.Column(db.String(10), default='秘密')
    # 字数
    charactors = db.Column(db.Integer, default=0)
    signature = db.Column(db.Text, default='这家伙很懒，什么都没有留下~')
    avatar = db.Column(db.String(300), default="https://donghaocms.oss-cn-beijing.aliyuncs.com/avater/default.jpg")

    # 保护字段
    @property
    def password(self):
        raise ArithmeticError("密码是不可读属性")

    #　生成hash
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 校验
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# 发帖
class PostsModel(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.String(150),primary_key=True,default=shortuuid.uuid)
    title = db.Column(db.String(150),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    # 阅读统计
    read_count = db.Column(db.Integer,default=0)
    # 作者ID 绑定
    author_id = db.Column(db.String(150),db.ForeignKey("user.id"))
    author = db.relationship("UserModel",backref='posts')

# 帖子和标签的关系表
post_tag = db.Table(
    'post_tag',
    db.Column('post_id',db.ForeignKey("posts.id"),primary_key=True),
    db.Column('tag_id',db.ForeignKey("tag.id"),primary_key=True)
)

# 标签
class TagsModel(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tagname = db.Column(db.String(150))
    posts = db.relationship("PostsModel",backref='tags',secondary=post_tag)

