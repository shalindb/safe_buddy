import flask
from flask import Flask, render_template, request, make_response, redirect, url_for
from dotenv import load_dotenv
import os
load_dotenv()
google_API_KEY = os.getenv("google_API_KEY")

app = Flask(__name__)

""" Home page to redirect to other pages (ie. input form or information)"""
@app.route('/', methods=['GET', 'POST'])
def index():
    #TODO
    if request.method == 'POST':
        if 'record' in request.form:
            return redirect(url_for('input'))
        elif 'timer' in request.form:
            return redirect(url_for('timer'))
        elif 'map' in request.form:
            return redirect(url_for("map"))
        elif 'info' in request.form:
            return redirect(url_for("info"))
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template('index.html')

""" Starting point, where client inputs user information """
@app.route('/input/')
def input():
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
    return render_template("timer.html")


""" Gets user location from ip address """
def get_location(ip_address):
    return None

""" Helpful locations map to link to safe injection facilities,
needle exchanges, Supervised Consumption Services, take-home naxolone centers,
housing, shelter, safe houses) """
@app.route('/map/', methods=['GET', 'POST'])
def map():
    # TODO 
    loc = request.environ['REMOTE_ADDR']
    query = "record+stores+in+Seattle"

    post_link = "https://www.googleapis.com/geolocation/v1/geolocate?key="
    post_link += google_API_KEY
    
    query_link = "https://www.google.com/maps/embed/v1/place?key="
    query_link += google_API_KEY
    query_link += "&q=" + query

    if request.method == 'POST':
        if 'record' in request.form:
            return redirect(url_for('input'))
        elif 'timer' in request.form:
            return redirect(url_for('timer'))
        elif 'map' in request.form:
            return redirect(url_for("map"))
        elif 'info' in request.form:
            return redirect(url_for("info"))
    elif request.method == 'GET':
        return render_template("map.html", query_link = query_link)
    return render_template("map.html", query_link = query_link)

""" Information (to link to more info dependong on type of drug) """
@app.route('/info/', methods=['GET', 'POST'])
def info():
    #TODO
    return render_template('info.html')

@app.route('/loc_getter', methods=['GET', 'POST'])
def loc_getter():
    if request.method == 'POST':
        print('Data:')
        print(request.get_json(force=True))
        data = request.get_json(force=True)
        return 'Archived.', 200


if __name__ == "__main__":
    app.run(debug=False, port=5000)
