import requests
from requests import post, get
import os
from dotenv import load_dotenv
import redis

load_dotenv()

redis = redis.Redis(host='containers-us-west-86.railway.app', password=os.getenv("REDIS_PASSWORD"), port='6624')

#  redis.set('mykey', 'Hello from Python!')
#  value = redis.get('mykey')
#  print(value)

#  redis.zadd('vehicles', {'car' : 0})
#  redis.zadd('vehicles', {'bike' : 0})
#  vehicles = redis.zrange('vehicles', 0, -1)
#  print(vehicles)
API_KEY = os.getenv("API_KEY")
HEADERS = {"x-dune-api-key": API_KEY}
BASE_URL = "https://api.dune.com/api/v1"

def make_api_url(module, action, id):
    return f"{BASE_URL}/{module}/{id}/{action}"

def execute_query(query_id):
    url = make_api_url("query", "execute", query_id)
    response = post(url, headers=HEADERS)
    return response.json()["execution_id"]

def get_query_results(execution_id):
    url = make_api_url("execution", "results", execution_id)
    response = get(url, headers=HEADERS)
    return response

# id = execute_query(1532121)
# print(id)
# print(get_query_results("01GH553ZX8VX5WTZVJD45AV3XV"))

# r = get_query_results('01GH553ZX8VX5WTZVJD45AV3XV')