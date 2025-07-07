from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, I'm Sahithi </p>"


# $ flask --app sah run
#  * Serving Flask app 'sah'
#  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)