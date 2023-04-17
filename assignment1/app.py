from flask import Flask, render_template, request
from utils.token_generator import generator 

app = Flask(__name__)

@app.route("/")
def login_user():
    return render_template('login/user.html')


@app.route("/admin")
def login_admin():
    return render_template('login/admin.html')


@app.route("/admin/dashboard", methods=['POST', 'GET'])
def send_login_info_admin():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        return render_template('dashboard/dashboard.html', result = result)
    return '<h4>Você precisa logar</h4>'


@app.route("/attendance", methods=['POST', 'GET'])
def send_login_info_user():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        return render_template('attendance/attendance.html', result = result)
    return '<h4>Você precisa logar</h4>'


@app.route("/newtoken", methods=['POST', 'GET'])
def generate_token():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        token = generator(json_result)
        return render_template('dashboard/dashboard.html', token = token)
    return '<h4>Error</h4>'

if __name__ == '__main__':
    app.run(debug = True)