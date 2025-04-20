from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    id_ast = StringField('Id астронавта', validators=[DataRequired()])
    password_ast = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_kap = StringField('Id капитана', validators=[DataRequired()])
    password_kap = PasswordField('Пароль капитана', validators=[DataRequired()])
