import imp
from flask import Flask, jsonify, request
app = Flask(__name__)
task = [
    {
        "Contact": "9987644456",
        "Name": "Raju",
        "done": False,
        "id": 1
    },
    {
        "Contact": "9876543222",
        "Name": "Rahul",
        "done": False,
        "id": 2
    }
]


@app.route("/")
def func1():
    return "r1"


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)
    task = {
        'id': task[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
    }
    task.append(task)
    return jsonify({"status": "success","message": "task added successfully"})

@app.route("/get-data")
def get_data():
    return jsonify({"data":task})

if(__name__ == "__main__"):
    app.run(debug=True)
