from flask import Flask, render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return hostname, host_ip

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/details")
def hello():
    hostname , ip = fetchDetails()
    return render_template('details.html', hostname=hostname, ip=ip)

if __name__ == "__main__":
    app.run(debug=True)