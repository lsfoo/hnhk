# coding utf-8
from flask_script import Manager, Server
from flask_admin import Admin
from flask_migrate import Migrate,MigrateCommand
import main 
import models

from flask_restful import  Api
from apis import HelloWorld

manager = Manager(main.app)
migrate = Migrate(main.app,models.db)

manager.add_command("server",Server())
manager.add_command("db",MigrateCommand)

admin = Admin(main.app,name='admin',template_mode='bootstrap3')
@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=main.app,
                db=models.db,
                Tag=models.Tag,
                Post=models.Post,
                Comment=models.Comment,
                User=models.User)

manager.add_command("runserver", Server())


api = Api(main.app)
api.add_resource(HelloWorld,'/h')

if __name__ == "__main__":
    manager.run()
