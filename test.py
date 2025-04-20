from flask import Flask, render_template, request, redirect, url_for
from login_form import LoginForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/table/<sex>/<int:years>')
def index(sex, years):
    if years < 21:
        if sex == 'male':
            wall_color = '#B0C4DE'
        else:
            wall_color = '#FFC0CB'
        image = '/static/img/child.png'
    else:
        if sex == 'male':
            wall_color = '#6495ED'
        else:
            wall_color = '#FA8072'
        image = '/static/img/adult.png'
    return render_template('auto_answer.html', wall_color=wall_color, image=image)

if __name__ == '__main__':
    app.run(port=5252, host='127.0.0.1')