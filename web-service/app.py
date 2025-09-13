from flask import Flask
import requests
import os


app=Flask(__name__)

ANALYTICS_URL=os.environ.get("ANALYTICS_URL","http://analytics:5001/visit")
@app.route('/')
def home():
	requests.get(ANALYTICS_URL)
	return "Hello from web Service!"

@app.route('/about')
def about():
	return "Web Service in Microservices Demo"

@app.route('/newRoute')
def newRoute():
	return "This is a New Route"

if __name__=="__main__":
	app.run(host='0.0.0.0',port=5000)

