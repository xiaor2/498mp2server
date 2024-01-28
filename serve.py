from flask import Flask, request
import subprocess
import socket

application = Flask(__name__)

@application.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		subprocess.Popen(['python', 'stress_cpu.py'])
		return 'CPU stress test initiated.', 202
	else:
		ip_address = socket.gethostbyname(socket.gethostname())
		return ip_address, 200

if __name__ == "__main__":
	application.run(host='0.0.0.0', port='8080')
