from flask import Flask, render_template, request, redirect, url_for
from login_form import LoginForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/table/<sex>/<int:years>')
def index(sex, years):
    if years < 21:
        if sex == 'male':
            wall_color = '#B0C4DE'  # Светло-голубой для молодого мужчины
        else:
            wall_color = '#FFC0CB'  # Розовый для молодой женщины
        image = '/static/img/child.png'  # Изображение для молодых
    else:
        if sex == 'male':
            wall_color = '#6495ED'  # Темно-синий для взрослого мужчины
        else:
            wall_color = '#FA8072'  # Красный для взрослой женщины
        image = '/static/img/adult.png'  # Изображение для взрослых
    return render_template('auto_answer.html', wall_color=wall_color, image=image)

if __name__ == '__main__':
    app.run(port=5252, host='127.0.0.1')