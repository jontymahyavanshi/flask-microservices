from flask import Flask 
import redis 
import os

app=Flask(__name__)
r=redis.Redis(host=os.environ.get("REDIS_HOST","redis"),
port=int(os.environ.get("REDIS_PORT",6379)))

@app.route('/visit')
def visit():
	count=r.incr("visit")
	return f"Total visits: {count}"
if __name__=="__main__":
	app.run(host='0.0.0.0',port=5001)

