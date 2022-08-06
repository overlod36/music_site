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

def get_list(st):
	return(list(st.replace(', ', '|').split('|')))

def group_file_saver(field, group_name):
	file = request.files[field]
	filename = secure_filename(file.filename)
	file.save(os.path.join(f'pack/static/models_images/{group_name}' , filename))
	return filename

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
		file.save(os.path.join(f'pack/models_images/{form.group_field.data}', filename))
		new_album = models.Album(title=form.title_field.data, group_name=form.group_field.data, release_date=form.date_field.data, producers_name=form.producers_field.data, duration=get_time(str(form.duration_field.data)[11:]), songs=get_list(form.songs_field.data), cover_path=filename, active_years=get_list(form.genres_field.data))
		db.session.add(new_album)
		db.session.commit()
		return redirect(url_for('main'))
	return render_template('add_alb_page.html', form=form)

@app.route('/add_group', methods=['GET', 'POST'])
def add_group():
	form = forms.Group_Form()
	if request.method == 'POST':
		if not os.path.exists(f'pack/static/models_images/{form.name_field.data}'):
			os.mkdir(f'pack/static/models_images/{form.name_field.data}')

		st = [group_file_saver('cover_field', form.name_field.data), group_file_saver('add_cover_field', form.name_field.data), group_file_saver('logo_field', form.name_field.data)]
		new_group = models.Group(name=form.name_field.data, main_cover_path=st[0], addin_cover_path=st[1], logo_path=st[2], current_members=get_list(form.current_members_field.data), past_members=get_list(form.past_members_field.data), active_years=form.active_years.data)
		db.session.add(new_group)
		db.session.commit()
		return redirect(url_for('main'))
	return render_template('add_group_page.html', form=form)



@app.route('/albums', methods=['GET', 'POST'])
def albums_page():
	albums = db.session.query(models.Album).all()
	return render_template('albums.html', albums=albums)

@app.route('/groups', methods=['GET', 'POST'])
def groups_page():
	groups = db.session.query(models.Group).all()
	return render_template('groups.html', groups=groups)

@app.route('/album/<name>')
def album_page(name):
	album = db.session.query(models.Album).filter_by(title=name).first()
	return render_template('el_album.html', album=album)

@app.route('/group/<name>')
def group_page(name):
	group = db.session.query(models.Group).filter_by(name=name).first()
	return render_template('el_group.html', group=group)