from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def prof(profession):
    return render_template('list_prof.html', profession=profession)


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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
