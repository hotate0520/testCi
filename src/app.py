from flask import Flask

app = Flask(__name__)

print("FLASK_VERSION")

@app.route("/")
def hello():
    return "Hello Docker V1"

app.run(host="0.0.0.0", port=8080)