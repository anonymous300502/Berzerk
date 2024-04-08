from flask import Flask, request, jsonify
import threading

lastlen = 0
app = Flask(__name__)
users = set()
@app.route("/4ee2ce1e")
def hello_world():
    global lastlen
    obj1 = request.headers.get('X-1412-93e6')
    users.add(obj1)
    print(users)
    return 'None'

app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
