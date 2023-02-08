from flask import Flask, jsonify, request

# app = Flask(__name__)

#@app.route('/')
def index():
    return "Hello, World!"

# @app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        # process the data and save it
        return jsonify({'message': 'Data received'})
    else:
        # retrieve the data and return it
        return jsonify({'data': 'example data'})

# if __name__ == '__main__':
#    app.run(debug=True)


'''
This creates a simple Flask API with two endpoints: 
/ and /api/data. The / endpoint returns a "Hello, World!" message, 
while the /api/data endpoint allows for both GET and POST requests. 
In the case of a POST request, the data is retrieved from the 
request using request.get_json() and can then be processed and saved. 
In the case of a GET request, the endpoint returns example data.

'''

