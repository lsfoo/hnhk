from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import app
db = SQLAlchemy(app)

posts_tags = db.Table('posts_tags',
        db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
        db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    introduction = db.Column(db.Text())
    identifier = db.Column(db.String(45))
    thumb_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    sort = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    category_id = db.Column(db.String(45), db.ForeignKey('categories.id'))
    type_id = db.Column(db.String(45), db.ForeignKey('types.id'))
    attachments = db.relationship(
            'Attachment',
            backref='posts',
            lazy='dynamic')


    comments = db.relationship(
            'Comment',
            backref='posts',
            lazy='dynamic')
    tags = db.relationship(
            'Tag',
            secondary=posts_tags,
            backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
            'Post',
            backref='users',
            lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "<Model User `{}`>".format(self.username)


class Attachment(db.Model):
    __tablename__ = 'attachments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    text = db.Column(db.Text())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))
    create_date = db.Column(db.DateTime)
    def __init__(self, name):
        self.name = name 

    def __repr__(self):
        return "<Model Attachment `{}`>".format(self.name)

class Category(db.Model):

    __tablename__ = 'categories'
    id = db.Column(db.String(45), primary_key=True)
    name  = db.Column(db.String(255))
    identifier = db.Column(db.String(45))

    posts = db.relationship(
            'Post',
            backref='categories',
            lazy='dynamic')

    def __init__(self, name):
        self.url = name 

    def __repr__(self):
        return "<Model Category `{}`>".format(self.name)

class Type(db.Model):

    __tablename__ = 'types'
    id = db.Column(db.String(45), primary_key=True)
    name  = db.Column(db.String(255))
    identifier = db.Column(db.String(45))

    posts = db.relationship(
            'Post',
            backref='types',
            lazy='dynamic')
    def __init__(self, name):
        self.url = name 

    def __repr__(self):
        return "<Model Type `{}`>".format(self.name)

class Page(db.Model):

    __tablename__ = 'pages'
    id = db.Column(db.String(45), primary_key=True)
    name  = db.Column(db.String(255))
    identifier = db.Column(db.String(45))
    template_path  = db.Column(db.String(255))
    def __init__(self, name):
        self.url = name 

    def __repr__(self):
        return "<Model Page `{}`>".format(self.name)

class Field(db.Model):
    __tablename__ = 'fields'
    id = db.Column(db.String(45), primary_key=True)
    key = db.Column(db.String(45))
    value  = db.Column(db.String(255))
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))
    def __init__(self, key):
        self.key = name 

    def __repr__(self):
        return "<Model Field `{}`>".format(self.key)

class Banner(db.Model):
    __tablename__ = 'banners'
    id = db.Column(db.String(45), primary_key=True)
    url = db.Column(db.String(255))
    link = db.Column(db.String(255))
    remark = db.Column(db.String(255))
    sort = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))
    def __init__(self, url):
       self.url = url 

    def __repr__(self):
        return "<Model Banner `{}`>".format(self.url)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String(45), primary_key=True)

    name = db.Column(db.String(255))
    price = db.Column(db.Numeric(10,2))
    create_date = db.Column(db.DateTime)

    def __init__(self, name):
       self.url = url 

    def __repr__(self):
        return "<Model Product `{}`>".format(self.name)

