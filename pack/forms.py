from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, DateTimeField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf.file import FileField

class Album_Form(FlaskForm):
	title_field = StringField('Название альбома', validators=[InputRequired(), Length(min=1, max=30)])
	group_field = StringField('Название группы', validators=[InputRequired(), Length(min=1, max=30)])
	date_field = DateField('Дата релиза', validators=[InputRequired()])
	producers_field = StringField('Продюссер альбома', validators=[InputRequired(), Length(min=5, max=30)])
	duration_field = DateTimeField('Длительность альбома', validators=[InputRequired()], format='%H:%M:%S')
	songs_field = StringField('Песни альбома', validators=[InputRequired(), Length(min=10, max=450)])
	cover_field = FileField()
	genres_field = StringField('Жанры', validators=[InputRequired()])
	submit = SubmitField('Добавить')


class Group_Form(FlaskForm):
	name_field = StringField('Название группы', validators=[InputRequired(), Length(min=1, max=40)])
	cover_field = FileField()
	add_cover_field = FileField()
	logo_field = FileField()
	current_members_field = StringField('Текущие участники', validators=[InputRequired()])
	past_members_field = StringField('Прошлые участники', validators=[InputRequired()])
	active_years = StringField('Годы активности', validators=[InputRequired()])
	submit = SubmitField('Добавить')