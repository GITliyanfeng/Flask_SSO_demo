import os

from datetime import timedelta
from flask import Flask, session, redirect, url_for, request
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds=24 * 60 * 60)


@app.route('/')
def index():
    session.permanent = False
    ticket = request.args.get('ticket', None)
    if ticket is not None:
        session['name'] = ticket.strip()
    # 检测当前站点的登陆状态session会话中是否有name
    if 'name' in session:
        return 'aw成功登陆'
    else:
        referer = requests.utils.quote('http://www.aw.com:5002/')
        return redirect('http://www.sso.com:5003/login?referer=' + referer)


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=int('5002'),
        debug=True
    )
