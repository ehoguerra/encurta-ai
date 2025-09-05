from flask import Blueprint, render_template, redirect, request, flash
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from uuid import uuid4
from db import db

bp = Blueprint('auth', import_name='auth', url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user=user, remember=remember)
            return redirect('/')
        else:
            flash('Credenciais incorretas', 'error')
            return render_template('login.html')
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_email = User.query.filter_by(email=email).first()
        existing_username = User.query.filter_by(username=username).first()

        if existing_email:
            flash('Este email já está cadastrado', 'error')
            return render_template('register.html')
        
        if existing_username:
            flash('Este nome de usuário já está em uso', 'error')
            return render_template('register.html')

        user = User(username=username, email=email, password=generate_password_hash(password))
        
        db.session.add(user)
        db.session.commit()
        
        login_user(user=user, remember=True)

        flash('Registrado com sucesso!', 'success')
        return redirect('/')

    return render_template('register.html')

@bp.route('/logout')
def logout():
    logout_user()
    flash('Você foi desconectado', 'success')
    return redirect('/')