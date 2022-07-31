from pack import app
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask_bootstrap import Bootstrap
from datetime import datetime
from pack import forms, db, models

def get_time(st):
	return datetime.strptime(st, '%H:%M:%S').time()

Bootstrap(app)

@app.route('/')
def main():
	return render_template('home.html')

@app.route('/add_album', methods=['GET', 'POST'])
def add_alb():
	form = forms.Album_Form()
	if request.method == 'POST':
		new_album = models.Album(title=form.title_field.data, group_name=form.group_field.data, release_date=form.date_field.data, producers_name=form.producers_field.data, duration=get_time(str(form.duration_field.data)[11:]), songs=["dssf", "qsaadd"])
		db.session.add(new_album)
		db.session.commit()
		return redirect(url_for('main'))
	return render_template('add_alb_page.html', form=form)

