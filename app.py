from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

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
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
