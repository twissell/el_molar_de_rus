#!/usr/bin/env python

"""
Project documentation.
"""

__author__ = "twissell"
__copyright__ = "Copyright 2013, The project-name Project"
__credits__ = ["twissell"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "twissell"
__email__ = "twissel.development@gmail.com"
__status__ = "Prototype"

# import builtins
# import third-party
from flask.ext.script import Manager, Server
from app import app
# import own

manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0'))
app.config['DEBUG'] = True


if __name__ == "__main__":
    manager.run()
