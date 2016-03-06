"""Models and database functions"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.sql import label
import requests, os, operator 
from sqlalchemy.dialects.postgresql import JSON
import psycopg2



db = SQLAlchemy()


####################################################################
#Model definitions

class User(db.Model):


	__tablename__='users'

	user_id = db.Column(db.String(50), primary_key=True)
	user_name = db.Column(db.String(50), nullable=True)
	audio_file = db.Column(db.String(100), nullable=True)
	url = db.Column(db.String(100), nullable=True)
	twitter_handle = db.Column(db.String(20), nullable=True)
	

	def __repr__(self):
		"""prints useful info on legislator"""

		return "<_id=%s>" % (self.user_id)


##############################################################################
# Helper functions for flask app

def connect_to_db(app):
    """Connect the database to our Flask app."""
    
    # Configure to use postgresql database
    DATABASE_URL = os.environ.get("DATABASE_URL", 'postgresql://ubuntu@localhost:5432/dubit')

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print "Connected to DB."

