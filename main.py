import flask
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

""" Starting point, where client inputs user information """

@app.route('/start')
def start():
    return render_template('input_form.html')


""" Sets client information to the request object's cookies and prompts emergency form
Access cookies: flask.request.cookies (type:dict) """

# NOTE: Still need to make emergency form default the contact number to 911 if the person chooses not to respond
@app.route('/set_user_info/', methods=['POST', 'GET'])
def set_user_info():
    if request.method == 'POST':
        name, age, drug_type = request.form.values()

        resp = flask.make_response(render_template('emergency_form.html', name=name))
        resp.set_cookie('Name', name)
        resp.set_cookie('Age', age)
        resp.set_cookie('Drug', drug_type)
        # now can access using flask.request.cookies (dictionary containing key,value pairs for client input)
        return resp


""" Sets the emergency contact information to the request object's cookies and prompts timer interface
Access cookies: flask.request.cookies (type:dict) """

@app.route('/timer/', methods=['POST', 'GET'])
def timer():
    if request.method == 'POST':
        c_name, c_phone = request.form.values()

        c_resp = make_response(render_template('timer.html'))
        c_resp.set_cookie('Contact Name', c_name)
        c_resp.set_cookie('Contact Phone', c_phone)

        return c_resp


""" Home page to redirect to other pages (ie. input form or information)"""
@app.route('/')
def index():
    #TODO
    # if request.method == 'POST':
    #     if request.form['submit_button'] == "Record Info":
    #         return redirect(url_for('start'))
    #     elif request.form['submit_button'] == "Safety Timer":
    #         return redirect(url_for('timer'))
    #     elif request.form['submit_button'] == "Nearby Resources":
    #         return redirect(url_for("map"))
    #     elif request.form['submit_button'] == "Information":
    #         return redirect(url_for("info"))
    # elif request.method == 'GET':
    #     return render_template('index.html')
    return render_template('index.html')

""" Helpful locations map to link to safe injection facilities,
needle exchanges, Supervised Consumption Services, take-home naxolone centers,
housing, shelter, safe houses) """
@app.route('/map/')
def helpful_map():
    # TODO 
    loc = request.environ['REMOTE_ADDR']
    
    return 'location %s' %loc

""" Information (to link to more info dependong on type of drug) """
@app.route('/info/')
def info():
    #TODO

    return flask.render_template('info.html')

if __name__ == "__main__":
    app.run(debug=False, port=5000)
