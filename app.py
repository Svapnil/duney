from flask import Flask
from dune import execute_query, get_query_results, get_ens_query_execution_id
import redis
import os

app = Flask(__name__)
redis = redis.StrictRedis(host='containers-us-west-86.railway.app', password=os.getenv("REDIS_PASSWORD"), port='6624', charset="utf-8", decode_responses=True)

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

@app.route('/<ens_domain>')
def get_ens_info(ens_domain):
  exec_id = get_ens_query_execution_id(ens_domain)

  # Have we already run this query?
  if redis.exists(f"{ens_domain}.exec_id"):
    exec_id = redis.get(f"{ens_domain}.exec_id")
    r = get_query_results(exec_id)
    if (r.json()["state"] == "QUERY_STATE_EXECUTING"):
        return "We are still executing the query for %s.eth" % ens_domain
    else:
        return build_result_output(r)
  else:
    exec_id = get_ens_query_execution_id(ens_domain)
    redis.set(f"{ens_domain}.exec_id", exec_id)
    return """
      <div>
        We are executing your ENS query now for the %s.eth username! Check back in a minute or two for the result!
      </div>
    """ % ens_domain
#   return """
#     <div>%s</div>
#   """ % ens_domain

def build_result_output(response):
    print(response.json())

    result = response.json().get("result")["rows"]
    if len(result) == 0:
        return "No results found"

    output = result[0]
    return """
        <div>
            <p>Here's an example of data you can get from the Dune API!!</p>
            <p>This is information that has been retrieved by using Dune to lookup the .eth addres svapnil.eth</p>
            <p>Check out the origin of this query <a href="https://dune.com/queries/1531883">here<a>:</p>
            <h3>Address</h3>
            <p>%s</p>
            <h3>Name</h3>
            <p>%s</p>
            <h3>Last Tx</h3>
            <p>%s</p>
        </div>
        """ % (result["address"], result["name"], result["latest_tx"])

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

