import flask
from flask import Flask, render_template, request, make_response, redirect, url_for, jsonify
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

    query_link = "https://www.google.com/maps/embed/v1/search?key="
    query_link += google_API_KEY


    return render_template("map.html", query_link = query_link)

""" Information (to link to more info depending on type of drug) """
@app.route('/info/', methods=['GET', 'POST'])
def info():
    return render_template('info.html')

@app.route('/depressants/', methods=['GET', 'POST'])
def depressants():
    return render_template('depressants.html')

@app.route('/stimulants/', methods=['GET', 'POST'])
def stimulants():
    return render_template('stimulants.html')

@app.route('/hallucinogens/', methods=['GET', 'POST'])
def hallucinogens():
    return render_template('hallucinogens.html')

@app.route('/multiclass/', methods=['GET', 'POST'])
def multiclass():
    return render_template('multiclass.html')

# @app.route('/loc_getter', methods=['GET', 'POST'])
# def loc_getter():
#     if request.method == 'POST':
#         data = request.get_json(force=True)
#         query = "record+stores+in+Seattle"
#         query_link = f'https://www.google.com/maps/embed/v1/search?key={google_API_KEY}&q={query}'
#         query_link += '&center='+ str(data['lat']) + ',' + str(data['lng'])
#         print("QUERYL:", query_link)
#         # resp = make_response(render_template('map.html'), query_link=query_link)
#         # resp.set_cookie('Latitude', str(data['lat']))
#         # resp.set_cookie('Longitude', str(data['lng']))
#
#         return render_template(('map.html'), query_link=query_link)
"""
                             // POST
            fetch('/map', { 

                // Specify the method
                method: 'POST',

                // A JSON payload
                body: JSON.stringify(pos)
            }).then(function (response) { // At this point, Flask has printed our JSON
                return response.text();
            }).then(function (text) {

                console.log('POST response: ');

                // Should be 'OK' if everything was successful
                console.log('Success.');
            });
"""




if __name__ == "__main__":
    app.run(debug=False, port=5100)
