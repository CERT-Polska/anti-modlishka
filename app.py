import os
from subprocess import Popen, PIPE

from flask import Flask, render_template, session, request
from flask_session import Session
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)

s = URLSafeTimedSerializer(app.config['SECRET_KEY'])


@app.route('/gen-js')
def gen_js():
    js_check_token = session.get('js_check_token')

    if not js_check_token:
        js_check_token = s.dumps({"sid": session.sid, "ip": request.remote_addr})

    process = Popen(["./obfuscate.js", js_check_token, app.config['LEGITIMATE_HOST']], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    return output


@app.route('/js-iframe')
def js_iframe():
    return render_template('js-iframe.html', rand_val=os.urandom(8).hex())


@app.route('/js-check/<token>')
def js_check(token):
    obj = s.loads(token, max_age=60)

    if obj.get('ip') == request.remote_addr and obj.get('sid') == session.sid:
        session['js_ok'] = True

    return ''


@app.route('/login', methods=['POST'])
def login():
    if not session.get('js_ok', False):
        return render_template('login.html', status='fraud')

    if request.form['login'] == 'demo' and request.form['password'] == 'demo':
        return render_template('login.html', status='ok')

    return render_template('login.html', status='error')


@app.route('/')
def hello_world():
    return render_template('index.html', rand_val=os.urandom(8).hex(), js_ok=session.get('js_ok', False))


if __name__ == '__main__':
    app.run()
