from flask import Flask
import os
from db import db, migrate
from routes.link_routes import bp as link_bp
from routes.oauth import bp as auth_bp
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mysecret')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')

db.init_app(app)
migrate.init_app(app, db)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(link_bp, name='main')
app.register_blueprint(auth_bp, name='auth')

if __name__ == '__main__':
    app.run(debug=True)