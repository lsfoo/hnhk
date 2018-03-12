# coding utf-8
from flask_script import Manager, Server
import main 
import models

manager = Manager(main.app)
@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=main.app,
                db=models.db,
                User=models.User)

manager.add_command("runserver", Server(host='0.0.0.0',port=80))

if __name__ == "__main__":
    manager.run()
