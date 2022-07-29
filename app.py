from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

def load_key():
	return open('setup/secret_key.txt', 'r').read()

app = Flask(__name__)
app.config['SECRET_KEY'] = load_key()

@app.route('/')
def main():
	return 'Hello!'

if __name__ == '__main__':
	app.run(debug=True)