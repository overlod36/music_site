from pack import db
from sqlalchemy import Column, String, Integer, Date, Time
from sqlalchemy.dialects.postgresql import ARRAY

class Group(db.Model):
	__tablename__ = "group"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	

class Album(db.Model):
	__tablename__ = "album"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), unique=True, nullable=False)
	release_date = db.Column(db.Date, nullable=False)
	producers_name = db.Column(db.String(100))
	duration = db.Column(db.Time, nullable=False)
	songs = db.Column(ARRAY(db.String(100)), nullable=False)

	def __repr__(self):
		return f'Album |{self.title}|\n release date >> {self.release_date}\n duration >> {self.duration}'

