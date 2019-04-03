import os

from datetime import timedelta
from flask import Flask, session, redirect, url_for, request, render_template
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds=24 * 60 * 60)


@app.route('/')
def index():
    session.permanent = False
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=int('5002'),
        debug=True
    )
