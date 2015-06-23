#!Flask/bin/python
from flask import Flask, render_template, session, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lucera'

class NameForm(Form):
    name = StringField('Enter Text: ', validators = [Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return '<h1>Sobreviure</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/game', methods = ['GET', 'POST'])
def game():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('game'))
    return render_template('game.html', form=form, name=session.get('name'))

if __name__ == '__main__':
 app.run(host = "192.168.2.226", debug=True)
