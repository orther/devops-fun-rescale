from flask import Flask, request, jsonify
import requests
application = Flask(__name__)

@application.route('/')
def dashboard():
    result = requests.get('http://0.0.0.0:5001/hardware/').json()
    hardware = [
        '{} - {}: {}'.format(r['provider'], r['name'], r['availability'])
        for r in result
    ]

    return '<br>'.join(hardware)

@application.route('/health_check')
def health_check():
  result = requests.get('http://0.0.0.0:5001/health_check').json()

  return jsonify({ "status": 'up' })

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
