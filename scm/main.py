from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from extensions import db

from routes.user_routes import users_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(users_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)