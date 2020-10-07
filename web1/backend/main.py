#!/usr/bin/env python3
import subprocess
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADER'] = 'Content-Type'
CORS(app)

@app.route('/')
def home():
    return 'Hello world'

@app.route('/nslookup', methods=['POST'])
def nslookup():
    if request.method == 'POST':
        content = request.json
        domain = content['domain']
        result = subprocess.run("nslookup %s" % domain, shell=True, check=True, stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
        return {
            'domain': domain,
            'data': '{}'.format(result.stdout.decode('utf-8').replace('\n', '<br>'))
        }
    else:
        return {
            'data': 'Requete Get non accepté'
        }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
