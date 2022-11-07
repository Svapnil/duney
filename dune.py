import os
from dotenv import load_dotenv
from requests import post, get

API_KEY = os.getenv("API_KEY")
HEADERS = {"x-dune-api-key": API_KEY}
BASE_URL = "https://api.dune.com/api/v1"

def make_api_url(module, action, id):
    return f"{BASE_URL}/{module}/{id}/{action}"

def execute_query(query_id):
    url = make_api_url("query", "execute", query_id)
    response = post(url, headers=HEADERS)
    return response.json()["execution_id"]

def get_ens_query_execution_id(ens_domain):
    url = make_api_url("query", "execute", 1531883)
    data = {"ens_domain": f"{ens_domain}.eth"}
    response = post(url, json={"query_parameters": data}, headers=HEADERS)
    return response.json()["execution_id"]

def get_query_results(execution_id):
    url = make_api_url("execution", "results", execution_id)
    response = get(url, headers=HEADERS)
    return response