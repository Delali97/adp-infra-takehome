# adp-infra-takehome


How to Run
* Build Docker image 
  docker image build -t adp . 
* Start Container
    docker run -p 5001:5001 -d --name adp_container adp

How to tear down container
    docker stop adp_container && docker rm adp_container


Setting the Log Level
- To display the debug logs set the logging level on line 12 in app.py from logging.INFO to logging.DEBUG. 
This will show all log lines.


* Scripts and unit tests for verifying expected behavior 

* How to run unit test
    pytest app/home_test.py

* CURL REQUESTS
*  Sending GET request with accept header NOT SET

    -> curl --location --request GET 'localhost:5001/' 

    response: "Hello, World"

* Sending GET request with accept header SET to application/json
    
    -> curl --location --request GET 'localhost:5001/' --header 'Accept: application/json'

    response: "message": "Hello, World"

* Sending POST request 
    
    -> curl --location --request POST 'localhost:5001/'

    response: "message": "Empty POST request"
