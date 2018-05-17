from flask_script import Manager, Command, Server
from flask import Flask
from app import app
import config

manager = Manager(app)
manager.add_command('runserver', Server(use_debugger=False, use_reloader=False, passthrough_errors=True))
if __name__ == "__main__":
    manager.run()

