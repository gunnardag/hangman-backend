import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(120))
    user_id = db.Column(db.String(120))
    finished = db.Column(db.Boolean, default=False)
    tries = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()


class PrivateWord(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    word = db.Column(db.String(120))

    def create(self):
        db.session.add(self)
        db.session.commit()


def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def _create_database():
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gunnar/Backend/hangman/test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gunnar/botti/test.db'
    init_app(app)
    with app.app_context():
        try:
            db.create_all()
        except:
            pass


if __name__ == '__main__':
    _create_database()
