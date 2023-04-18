from flask import Flask, render_template, request
from flask import jsonify
import json
from utils.token_generator import generator 

app = Flask(__name__)

with open('mockdata/users.json', 'r') as mockUsers:
    data = mockUsers.read()

obj = json.loads(data)

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

@app.route("/api/user/getall", methods=['GET'])
def get_users():
    return jsonify(obj)


@app.route("/api/user/create", methods=['POST'])
def create_user():
    return 'create user'


@app.route("/api/user/update", methods=['UPDATE'])
def update_user():
    return 'update user'


@app.route("/api/user/delete", methods=['DELETE'])
def delete_user():
    return 'delete user'

if __name__ == '__main__':
    app.run(debug = True)