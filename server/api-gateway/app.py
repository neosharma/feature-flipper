from time import time
from flask import Flask, request
from flask_cors import CORS
import requests
import json
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return {"Message" : "API Gateway wrapper for lambda functions!"}

#adding variables
@app.route('/sets', methods=["GET"])
def get_sets():
  return call_lambda_function(request.method, request.path, "", "", "")

@app.route('/set/<set_id>', methods=["GET","PUT","DELETE"])
def crud_set_id(set_id):
  return call_lambda_function(request.method, "/set/{set_id}", "", set_id, "")

@app.route('/set/<set_id>/aliases', methods=["GET","POST"])
def set_alias(set_id):
  return call_lambda_function(request.method, "/set/{set_id}/aliases", request.json, set_id, "")

@app.route('/set', methods=["POST"])
def post_set():
  return call_lambda_function(request.method, request.path, request.json, "", "")

@app.route('/alias/<alias_id>', methods=["DELETE"])
def delete_alias_with_id(alias_id):
  return call_lambda_function(request.method, "/alias/{alias_id}", request.json, "", alias_id)

# API Gateway Request mapping
# {
#   "http_method": "$context.httpMethod",
#   "resource_path": "$context.resourcePath",
#   "body": $input.json('$'),
#   "headers": {
#     "if-match": "$input.params().header.get('If-Match')"
#   },
#   "set_id": "$input.params('set_id')",
#   "alias_id": "$input.params('alias_id')"
# }
def call_lambda_function(method, path, body, set_id, alias_id):
    body = {
        "http_method": method,
        "resource_path": path,
        "body": body,
        "set_id": set_id,
        "alias_id": alias_id
    }
    print('Payload: ' + json.dumps(body))
    headers = {"Accept": "application/json"}
    endpoint = "http://ff-private-api:8080/2015-03-31/functions/function/invocations"
    return requests.post(endpoint, json=body, headers=headers, timeout=3).json()
