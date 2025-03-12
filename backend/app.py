# TODO: UPDATE THIS FILE FOR DEPLOYMENT

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Creates a Flask application instance
app = Flask(__name__)
CORS(app)

# Configure SQLite database location
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
# Disable SQLAlchemy event system (improves performance)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialises SQLAlchemy
db = SQLAlchemy(app)

import routes

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)