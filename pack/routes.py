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
		#images.save(form.cover_field.data)
		file = request.files['cover_field']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'], filename))
		'''new_album = models.Album(title=form.title_field.data, group_name=form.group_field.data, release_date=form.date_field.data, producers_name=form.producers_field.data, duration=get_time(str(form.duration_field.data)[11:]), songs=get_songs(form.songs_field.data))
		db.session.add(new_album)
		db.session.commit()'''
		return redirect(url_for('main'))
	return render_template('add_alb_page.html', form=form)

