import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Words(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100))
    origin_language = db.Column(db.String(100))
    english_meaning = db.Column(db.String(100))
    learned = db.Column(db.Boolean(False))



 
