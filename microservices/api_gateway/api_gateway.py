#!/usr/bin/env python

# Matthew Klaczak
# mck70@pitt.edu

from flask import Flask
import requests

# Class that utilizes Pystache templating to generate server code with aid of Flask library for the API Gateway microservice
app = Flask(__name__)

@app.route("/", methods=['GET']) # Built-in HTTP method GET already included
def get_index():
    return 'You have reached the API-Gateway index page'

# This code template is used to automatically generate any and all server code on the fly.
# The resulting code will have a corresponding function for each HTTP method that is included in the API spec
 
@app.route('/pet', methods=['post'])
def update_pet(body,):
    microservice_response = requests.post("http://172.16.238.6:8080/pet",
        body,
    )
    return microservice_response.content
 
@app.route('/pet', methods=['get'])
def update_pets():
    microservice_response = requests.get("http://172.16.238.6:8080/pet",
        
    )
    return microservice_response.content
 
@app.route('/pet/{petId}', methods=['get'])
def find_by_id(petId,):
    microservice_response = requests.get("http://172.16.238.6:8080/pet/{petId}",
        petId,
    )
    return microservice_response.content
 
@app.route('/ui', methods=['get'])
def ui():
    microservice_response = requests.get("http://172.16.238.7:8080/ui",
        
    )
    return microservice_response.content
 
@app.route('/ui-yaml', methods=['get'])
def ui_yaml():
    microservice_response = requests.get("http://172.16.238.7:8080/ui-yaml",
        
    )
    return microservice_response.content
 
@app.route('/user', methods=['post'])
def register_customer(body,):
    microservice_response = requests.post("http://172.16.238.8:8080/user",
        body,
    )
    return microservice_response.content
 
@app.route('/user', methods=['get'])
def get():
    microservice_response = requests.get("http://172.16.238.8:8080/user",
        
    )
    return microservice_response.content
 
@app.route('/user/{customerId}', methods=['get'])
def get_user(customerId,):
    microservice_response = requests.get("http://172.16.238.8:8080/user/{customerId}",
        customerId,
    )
    return microservice_response.content

# Main method
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)