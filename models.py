from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """ Connect to database """
    
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()

class User(db.Model):
    
    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
          
    @classmethod
    def register(cls, username, pwd, em, first, last):
        """ Register user with hashed password and return user """
        
        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal string
        hashed_utf8 = hashed.decode("utf8")
        
        # return instance of user with hashed pwd 
        return cls(username=username, password=hashed_utf8, email=em, first_name=first, last_name=last)
    
    @classmethod
    def authenticate(cls, username, pwd):
        """ Authenticate user login credentials. 
        Return user if valid; else return False. """
        
        u = User.query.filter_by(username=username).first()
        
        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False

class Feedback(db.Model):
    
    __tablename__ = 'feedbacks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String, db.ForeignKey('users.username'))
    
    user = db.relationship('User', backref="feedbacks", cascade="all, delete")