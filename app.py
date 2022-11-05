from flask import Flask
from dune import execute_query, get_query_results

app = Flask(__name__)

@app.route("/")
def hello_world():
    r = get_query_results('01GH51AJPTG68BT06D7BMX74M1')
    return f"<div><p>Hello, World!</p><p>{r.json()}</p></p>"

# @app.route("/hello")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/world")
# def hello_world():
#     return "<p>Hello, World!</p>"
