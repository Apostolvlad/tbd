from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.web.auth import bp
from app.models import User
from app.web.auth.forms import LoginForm, RegistrationForm

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Ошибка логина или пароля.')
            return redirect(url_for('auth.login'))
        login_user(user, remember = form.remember_me.data)
    return render_template('auth/login.html', title = 'Авторизация', form = form)

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Успешно, вы создали нового пользователя!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title = 'Регистрация', form = form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))