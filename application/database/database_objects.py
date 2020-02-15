from flask_sqlalchemy import SQLAlchemy


class Team_Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    link = db.Column(db.String(20), unique=False, nullable=False)
    position = db.Column(db.String(20), unique=False, nullable=False)
    image_path = db.Column(db.String(60), unique=False, nullable=False)
    descrition = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return f"Team_member('{self.name}', '{self.position}', '{self.image_path}', '{self.description}')"