import flask
from flask import Flask

app = Flask(__name__)

@app.route('/start')
def start():
    return flask.render_template('input_form.html')

@app.route('/set_user_info', methods = ['POST', 'GET'])
def set_user_info():
    if flask.request.method == 'POST':
        name, age, drug_type = [elem for elem in flask.request.form.values()]
        #FOR DEBUGGING: return f'Name: {name}, Age: {age}, Drug: {drug_type}'



if __name__ == "__main__":
    app.run(debug=True, port=8180)