from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def load_key():
    return open('pack/setup/secret_key.txt', 'r').read()

def connect_to_db():
    args = []
    setup_f = open('pack/setup/server_setup.txt', 'r')
    for el in setup_f:
        args.append(el.replace('\n',''))
    return 'postgresql://{}:{}@{}:{}/{}'.format(args[0], args[1], args[2], args[3], args[4])


app = Flask(__name__)
app.config['SECRET_KEY'] = load_key()
app.config['SQLALCHEMY_DATABASE_URI'] = connect_to_db()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from pack import models, routes
