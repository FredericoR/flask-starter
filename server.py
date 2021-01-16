from flask import Flask, render_template, url_for
from markupsafe import escape
app = Flask(__name__)

# url_for('static', filename='text.txt')

@app.route('/')
@app.route('/<name>')
def hello(name='stranger'):
    return 'hi, %s! %s =)' % (escape(name), ('My friend.' if name != 'stranger' else ''))

@app.route('/welcome/')
@app.route('/welcome/<name>')
def welcome(name=None):
    return render_template('welcome.html', name=name)