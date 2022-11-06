from flask import Flask
from dune import execute_query, get_query_results

app = Flask(__name__)

@app.route("/")
def hello_world():
    r = get_query_results('01GH553ZX8VX5WTZVJD45AV3XV')
    print(r.json())
    final_result = r.json().get("result")["rows"][0]
    return """
        <div>
            <p>Here's an example of data you can get from the Dune API!!</p>
            <p>This is information that has been retrieved by using Dune to lookup the .eth addres svapnil.eth</p>
            <p>Check out the origin of this query <a href="https://dune.com/queries/1532121">here<a>:</p>
            <h3>Address</h3>
            <p>%s</p>
            <h3>Name</h3>
            <p>%s</p>
            <h3>Last Tx</h3>
            <p>%s</p>
        </div>
        """ % (final_result["address"], final_result["name"], final_result["latest_tx"])

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

# @app.route("/hello")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/world")
# def hello_world():
#     return "<p>Hello, World!</p>"
