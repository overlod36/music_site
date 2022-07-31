from pack import app
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask_bootstrap import Bootstrap
from pack import forms

Bootstrap(app)

@app.route('/')
def main():
	return render_template('home.html')

@app.route('/add_album', methods=['GET', 'POST'])
def add_alb():
	form = forms.Album_Form()
	if request.method == 'POST':
		return redirect(url_for('main'))
	return render_template('add_alb_page.html', form=form)