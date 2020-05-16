import flask
from flask import Flask

app = Flask(__name__)

""" Starting point, where client inputs user information """

@app.route('/start')
def start():
    return flask.render_template('input_form.html')


""" Sets client information to the request object's cookies and prompts emergency form
Access cookies: flask.request.cookies (type:dict) """

# NOTE: Still need to make emergency form default the contact number to 911 if the person chooses not to respond
@app.route('/set_user_info', methods=['POST', 'GET'])
def set_user_info():
    if flask.request.method == 'POST':
        name, age, drug_type = flask.request.form.values()

        resp = flask.make_response(flask.render_template('emergency_form.html', name=name))
        resp.set_cookie('Name', name)
        resp.set_cookie('Age', age)
        resp.set_cookie('Drug', drug_type)
        # now can access using flask.request.cookies (dictionary containing key,value pairs for client input)
        return resp


""" Sets the emergency contact information to the request object's cookies and prompts timer interface
Access cookies: flask.request.cookies (type:dict) """

@app.route('/timer', methods=['POST', 'GET'])
def timer():
    if flask.request.method == 'POST':
        c_name, c_phone = flask.request.form.values()

        c_resp = flask.make_response(flask.render_template('timer.html'))
        c_resp.set_cookie('Contact Name', c_name)
        c_resp.set_cookie('Contact Phone', c_phone)

        return c_resp


if __name__ == "__main__":
    app.run(debug=True, port=8280)
