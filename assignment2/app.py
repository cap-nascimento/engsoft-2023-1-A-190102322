from flask import Flask, render_template, request
from flask import jsonify
import json
import urllib.request, json
from utils.token_generator import generator 

import os

app = Flask(__name__)
app.config['NASA_API_KEY'] = 'OKsH8ppdd1FH0mrISWCpCB8UIzdZYvk5TpnUPy0i'

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
        return render_template('dashboard/imgsearch.html', result = result)
    return '<h4>Você precisa logar</h4>'


@app.route("/attendance", methods=['POST', 'GET'])
def send_login_info_user():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        return render_template('attendance/index.html', result = result)
    return '<h4>Você precisa logar</h4>'


@app.route("/newimage", methods=['POST', 'GET'])
def search_nasa_image():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        search_filter = 'mars-photos/api/v1/rovers/curiosity/photos'
        url = 'https://api.nasa.gov/{}?earth_date={}&api_key={}'.format(search_filter, json_result['earth_date'], os.environ.get('NASA_API_KEY'))
        return render_template('dashboard/imgsearch.html', url = url)

# @app.route("/newtoken", methods=['POST', 'GET'])
# def generate_token():
#     if request.method == 'POST':
#         result = request.form
#         json_result = dict(result)
#         token = generator(json_result)
#         return render_template('dashboard/dashboard.html', token = token)
#     return '<h4>Error</h4>'

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