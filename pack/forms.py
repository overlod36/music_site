from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, DateTimeField
from wtforms.validators import InputRequired, Length, ValidationError


class Album_Form(FlaskForm):
	title_field = StringField('Название альбома', validators=[InputRequired(), Length(min=1, max=30)])
	group_field = StringField('Название группы', validators=[InputRequired(), Length(min=1, max=30)])
	date_field = DateField('Дата релиза', validators=[InputRequired()])
	producers_field = StringField('Продюссер альбома', validators=[InputRequired(), Length(min=5, max=30)])
	duration_field = DateTimeField('Длительность альбома', validators=[InputRequired()], format='%H:%M:%S')
	songs_field = StringField('Песни альбома', validators=[InputRequired(), Length(min=10, max=450)])
	submit = SubmitField('Добавить')

