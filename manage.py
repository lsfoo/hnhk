# coding utf-8
from flask_script import Manager, Server
from flask_admin import Admin
from main import app
import models

from flask_restful import  Api
from apis import HelloWorld

manager = Manager(app)

admin = Admin(app,name='admin',template_mode='bootstrap3')
@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=main.app,
                db=models.db,
                User=models.User)

manager.add_command("runserver", Server(host='0.0.0.0',port=5000))


api = Api(app)
api.add_resource(HelloWorld,'/h')

if __name__ == "__main__":
    manager.run()
