import os

from datetime import timedelta
from flask import Flask, session, redirect, request, render_template,url_for
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds=30 * 24 * 60 * 60)


@app.route('/login')
def login():
    session.permanent = True
    referer = request.args.get('referer', None)
    if referer is not None:
        session['name'] = referer.strip()
    # 检测当前站点的登陆状态session会话中是否有name
    if 'name' in session:
        if referer is not None:
            return redirect(referer + '?ticket=' + _makeTicket())
    return render_template('login.html', **dict(referer=referer))


@app.route('/dologin')
def doLogin():
    session.permanent = True
    referer = request.args.get('referer', None)
    if referer is not None:
        referer = requests.utils.unquote(referer.strip())
    _setLoginState()
    if referer:
        return redirect(referer + '?ticket=' + _makeTicket())
    else:
        return 'error'


def _setLoginState():
    """添加登陆逻辑"""
    session['name'] = 'goal'


def _makeTicket():
    """添加加密算法生成ticket"""
    return 'goal'


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=int('5003'),
        debug=True
    )
