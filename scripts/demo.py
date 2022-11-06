import requests
from requests import post, get
import os
from dotenv import load_dotenv

load_dotenv()

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
print(id)
print(get_query_results("01GH553ZX8VX5WTZVJD45AV3XV"))

r = get_query_results('01GH553ZX8VX5WTZVJD45AV3XV')