from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/post', methods=['POST'])
def handle_post_request():
  # Get the data from the request
  data = request.get_json()

  # Load the existing data from the JSON file
  with open('data.json', 'r') as f:
      existing_data = json.load(f)

  # Add the new data to the existing data
  existing_data.update(data)

  # Save the updated data to the JSON file
  with open('data.json', 'w') as f:
      json.dump(existing_data, f,indent=3)

  return jsonify('Success')


@app.route('/get', methods=['GET'])
def handle_get_request():
  if request.method == 'GET':
    # Get the request data as a dictionary
    getData = request.args.to_dict()
    with open('data.json', 'r') as f:
      data = json.loads(f.read())
    return jsonify(data)
    # Do something with the data
    # ...

    # Return a response to the client



if __name__ == '__main__':
 
    app.run(debug="True")