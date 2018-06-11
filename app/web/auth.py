from flask import render_template, request, redirect, url_for, flash

from app.forms.register import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web

@web.route('/register', methods=['GET', 'POST'])
def register():
    wtform = RegisterForm(request.form)
    if request.method=='POST' and wtform.validate():
        user=User()
        user.set_attr(wtform.data)
        # user.nickname=wtform.nickname.data
        # user.email=wtform.email.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html',form=wtform)


@web.route('/login', methods=['GET', 'POST'])
def login():
    wtform=LoginForm()
    if request.method=='POST' and wtform.validate():
        user=User.query.filter(email=wtform.email.data).first()
        if user and user.check_password(user.password):
            pass
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html',form=wtform)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
