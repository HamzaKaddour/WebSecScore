from flask import Flask, request, jsonify
from scoring import mainScanner  # Replace with the actual import for your scanner code

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json

    domain = data.get("domain")
    company_name = data.get("companyName") if data.get("companyName") else None

    if not domain:
        return jsonify({"error": "Domain is required"}), 400

    # Run the mainScanner function
    result = mainScanner(domain, company_name)

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)