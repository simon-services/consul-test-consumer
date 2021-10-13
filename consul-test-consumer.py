from flask import Flask
import requests
import os
 
app = Flask(__name__)
 
@app.route('/')
def get_consumer():
    response = requests.get("http://127.0.0.1:6001/")
    res='[{"service":"consul-test-consumer", "consumer":"consul-test-consumer"},'
    return res + response.content.decode('utf-8') + ']\n'
 
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)
