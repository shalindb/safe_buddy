import flask
from flask import Flask

app = Flask(__name__)


@app.route('/start')
def start():
    return flask.render_template('input_form.html')


@app.route('/set_user_info', methods=['POST', 'GET'])
def set_user_info():
    if flask.request.method == 'POST':
        name, age, drug_type = flask.request.form.values()
        # FOR DEBUGGING: return f'Name: {name}, Age: {age}, Drug: {drug_type}'

        resp = flask.make_response(flask.render_template('emergency_form.html', name=name))
        resp.set_cookie('Name', name)
        resp.set_cookie('Age', age)
        resp.set_cookie('Drug', drug_type)
        # now can access using flask.request.cookies (dictionary containing key,value pairs for client input)
        return resp

@app.route('/timer')
def timer():
    if flask.request.method == 'POST':
        return flask.request.form.values()


# @app.route('/get_info')
# def get_info():
#     name = flask.request.cookies['Name']
#     age = flask.request.cookies['Age']
#     drug = flask.request.cookies['Drug']
#     return f'Hello {name}, of age {age}. You are addicted to {drug}.'


if __name__ == "__main__":
    app.run(debug=True, port=8180)
