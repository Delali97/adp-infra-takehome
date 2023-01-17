"""
module api contains a flask app with a single endpoint.
"""
from flask import Flask, json, jsonify
from flask import request, Response
import os
import http

import logging

# set logging levels (logging.INFO, logging.DEBUG, logging.ERROR)
logging_level = logging.INFO


logging.basicConfig(filename='ADP-INFRA-TAKEHOME.log', level=logging_level, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    app.logger.debug("Calling the Hello world request")
    if request.method == 'GET':
        if 'Accept' in request.headers:
            # Returns json 'hello world' when accept header = 'application/json'
            if request.headers.get('Accept') == 'application/json':
                app.logger.debug("request url:" + request.url + "Recieved an Accept Header='application/json'")
                return jsonify({'message': 'Hello, World'}) 
               
        else :
            app.logger.debug("request url:" + request.url + "Accept Header Is Empty")
            return '<p>Hello, World</p>'
    elif request.method == 'POST':
        #This is an empty POST request
        app.logger.debug("request url:" + request.url + "Empty POST request")
        return jsonify({'message': 'Empty POST request'})
    
if __name__ == '__main__':
    app.logger.debug("Starting App")
    port = int(os.environ.get('PORT', 5001))
    host = '0.0.0.0'
    app.run(debug=True, host=host, port=port)