# coding:utf-8
from flask import Flask
from config import DevConfig

app = Flask(__name__,static_url_path='')
app.config.from_object(DevConfig)

views = __import__('views')


if __name__ == '__main__':
    app.run()
