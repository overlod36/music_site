from pack import app
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask_bootstrap import Bootstrap
from datetime import datetime
from pack import forms, db, models, images
from werkzeug.utils import secure_filename
import os

def get_time(st):
	return datetime.strptime(st, '%H:%M:%S').time()

def get_songs(st):
	return(list(st.replace(', ', '|').split('|')))

Bootstrap(app)

@app.route('/')
def main():
	return render_template('home.html')

@app.route('/add_album', methods=['GET', 'POST'])
def add_alb():
	form = forms.Album_Form()
	if request.method == 'POST':
		file = request.files['cover_field']
		filename = secure_filename(file.filename)
		file.save(os.path.join('pack/static/albums', filename))
		new_album = models.Album(title=form.title_field.data, group_name=form.group_field.data, release_date=form.date_field.data, producers_name=form.producers_field.data, duration=get_time(str(form.duration_field.data)[11:]), songs=get_songs(form.songs_field.data), cover_path=filename)
		db.session.add(new_album)
		db.session.commit()
		return redirect(url_for('main'))
	return render_template('add_alb_page.html', form=form)

@app.route('/add_group', methods=['GET', 'POST'])
def add_group():
	form = forms.Group_Form()
	if request.method == 'POST':
		file = request.files['cover_field']
		filename = secure_filename(file.filename)
		file.save(os.path.join('pack/static/groups', filename))
		new_group = models.Group(name=form.name_field.data, cover_path=filename)
		db.session.add(new_group)
		db.session.commit()
		return redirect(url_for('main'))
	return render_template('add_group_page.html', form=form)



@app.route('/albums', methods=['GET', 'POST'])
def alb_page():
	albums = db.session.query(models.Album).all()
	return render_template('albums.html', albums=albums)

@app.route('/groups', methods=['GET', 'POST'])
def group_page():
	groups = db.session.query(models.Group).all()
	return render_template('groups.html', groups=groups)