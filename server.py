from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr_data', methods=['POST'])
def qr_data():
    data = request.form['qr_data']
    print("QR Code Data:", data)
    # hadling data here
    return 'Received'

if __name__ == '__main__':
    certfile = os.path.join(os.path.dirname(__file__), 'certs/cert.pem')
    keyfile = os.path.join(os.path.dirname(__file__), 'certs/key.pem')
    app.run(host='0.0.0.0', port=16888, ssl_context=(certfile, keyfile), debug=True)


