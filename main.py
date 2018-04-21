# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask,render_template
from config import DevConfig

app = Flask(__name__,static_url_path='')



app.config.from_object(DevConfig)



@app.route('/')
def home():
    return render_template('home.html',title='首页')




if __name__ == '__main__':
    app.run()
