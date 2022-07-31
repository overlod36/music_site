from pack import app
from flask import render_template
from flask import url_for
from flask import redirect
from flask_bootstrap import Bootstrap

@app.route('/')
def main():
	return 'Hello!'
