from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def prof(profession):
    return render_template('training.html', profession=profession)


@app.route('/list_prof/<params>')
def prof_list(params):
    if params != 'ol' and params != 'ul':
        return 'Неверный параметер'
    list_prof = ['Инженер', 'Врач', 'Офицер безопастности', 'Капитан',
                 'Штурман', 'Биолог', 'Психолог', 'Механик', 'Электрик']
    return render_template('list_prof.html', params=params, list1=list_prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {}
    params['title'] = 'Анкета'
    params['surname'] = 'Watny'
    params['name'] = 'Mark'
    params['education'] = 'выше среднего'
    params['profession'] = 'штурман марсохода'
    params['sex'] = 'male'
    params['motivation'] = 'Всегда мечтал застрять на Марсе'
    params['ready'] = 'True'
    return render_template('auto_answer.html', data=params)


class LoginForm(FlaskForm):
    id_astronaut = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    button = SubmitField('Доступ')
    if form.validate_on_submit():
        return 'done!'
    return render_template('login.html', title='Аварийный доступ', form=form, button=button)


@app.route('/distribution')
def distribution():
    data = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур']
    return render_template('distribution.html', data=data)


@app.route('/table/<sex>/<old>')
def table(sex, old):
    return render_template('table.html', sex=sex, old=int(old))


@app.route('/member')
def members_in_ship():
    data = os.path.join(app.root_path, 'templates', 'member.json')
    with open(data, encoding='utf-8') as f:
        members = json.load(f)
    random_member = random.choice(members)
    return render_template('member.html', member=random_member)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
