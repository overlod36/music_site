from pack import app
from flask import render_template
from flask import url_for
from flask import redirect
from flask_bootstrap import Bootstrap
from pack import forms

Bootstrap(app)

@app.route('/')
def main():
	return render_template('home.html')

@app.route('/add_album')
def add_alb():
	form = forms.Album_Form()
	return render_template('add_alb_page.html', form=form)