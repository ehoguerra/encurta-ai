from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user
from models.link import Link
from models.user import User
from db import db
from utils.utils import generateCode
import string

bp = Blueprint('/', import_name='main', url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        
        if 'https://' not in url and 'http://' not in url:
            url = f'https://{url}'

        if current_user and current_user.is_authenticated:
            code = request.form.get('custom_alias')
        else:
            code = generateCode()
        
        link = Link(original_url=url, short_code=code, user_id=current_user.id if current_user and current_user.is_authenticated else None)

        db.session.add(link)
        db.session.commit()
        flash(f'Link curto gerado: http://127.0.0.1:5000/{code}', 'success')
        return render_template('index.html', user=current_user)
    
    user_links = []
    if current_user and current_user.is_authenticated:
        user_links = Link.query.filter(Link.user_id == current_user.id).all()

    return render_template('index.html', user=current_user, user_links=user_links)

@bp.route('/<link_code>')
def redirect_link(link_code):
    link = Link.query.filter_by(short_code=link_code).first_or_404()
    return redirect(link.original_url)
