from flask import Flask, request
import requests

app = Flask(__name__)

# Azure Functions의 HTTP 트리거 URL
AZURE_FUNCTION_URL = "https://azureknu.azurewebsites.net"

@app.route('/')
def index():
    return 'Hello, this is a simple web application calling Azure Function!'

@app.route('/call_function', methods=['POST'])
def call_azure_function():
    name = request.form.get('name')
    if name:
        response = requests.post(AZURE_FUNCTION_URL, json={'name': name})
        return f"Azure Function response: {response.text}"
    else:
        return "Please provide a name."

if __name__ == '__main__':
    app.run(debug=True)
