from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    workouts = db.relationship('Workout', backref='date', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_type = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    exercises = db.relationship('Exercise', backref='exercise_name', lazy='dynamic')

    def __repr__(self):
        return f'<Workout {self.id}-{self.timestamp}>'

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    muscle_group = db.Column(db.String(64), index=True)
    muscle = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Exercise {self.name}>'
