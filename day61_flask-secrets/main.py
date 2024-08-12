from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "any-string-can-be-kept-secret"
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    email = login_form.email.data
    password = login_form.password.data
    if login_form.validate_on_submit() and email == "admin@email.com" and password == "12345678":
        return render_template('success.html')
    elif login_form.validate_on_submit() and (email != "admin@email.com" or password != "12345678"):
        return render_template('denied.html')
    else:
        return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
