from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, TimeField
from wtforms.validators import InputRequired, Length, ValidationError


class Album_Form(FlaskForm):
	title_field = StringField('Название альбома', validators=[InputRequired(), Length(min=1, max=30)])
	date_field = DateField('Дата релиза', validators=[InputRequired()])
	producers_field = StringField('Продюссер альбома', validators=[InputRequired(), Length(min=5, max=30)])
	duration_field = TimeField('Длительность альбома')
	submit = SubmitField('Добавить')