import os
from datetime import timedelta
from flask import Flask, session, request, make_response

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds=30 * 24 * 60 * 60)


@app.route('/setLoginState')
def setLoginState():
    session.permanent = True
    session['name'] = 'goal'
    session['nick'] = 'xxxxooooxxxx'
    resp = make_response('')
    resp.headers['P3P'] = 'CP="CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR"'
    return resp


@app.route('/test')
def test():
    session.permanent = True
    _str = ''
    if 'name' in session:
        _str = session['name']
    if 'nick' in session:
        _str += '---' + session['nick']
    return _str


if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5003"),
        debug=True
    )
