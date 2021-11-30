import flask, os ,sys , json
from flask import request, jsonify

app= flask.Flask(__name__)
app.config["DEBUG"] = True

#Create some test data for our catalog in the form of a list of dictionaries.


#fileObj=open("DeviceFile.txt","r ")
with open (os.path.join(sys.path[0],"ApiSimulator.json"),"r") as f:
    DummyMe_API= json.load(f)

#print(f.read())
#DummyMe_API = fileObj.readlines()

@app.route('/', methods=['GET'])
def home():
    return '''<h1> Dummy Me </h1>
<p> A prototype API page for parameters/specifications. </p>'''

@app.route('/api/v1/resources/devices/all', methods=['GET'])
def api_all():
    return jsonify(DummyMe_API)

@app.route('/api/v1/resources/devices', methods=['GET'])
def api_dates():

    if 'startDate' and 'endDate' in request.args:
        # Check if an StartDate or EndDate was provided as part of the URL.
        # If dates are provided, assign it to a variable.
        # If dates are not provided, display as an error in the browser.
        SDateTime = str(request.args['startDate'])
        EDateTime = str(request.args['endDate'])
        print(SDateTime)
        print(EDateTime)
    else:
        return "Error: No StartDate or EndDate feild provided. Please specify StartDate or EndDate"


    #Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested dates
    for dummyme_api in DummyMe_API:
        print(dummyme_api)

        if 1:
            results.append(dummyme_api)


    # Use the Jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.

    return jsonify(results)

    # Open a browser and hit below url
    # 127.0.0.1:5000/api/v1/resources/devices?startDate=2021-11-30-00:12:11&endDate=2021-11-30-00:12:11

app.run()