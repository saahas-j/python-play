#python code to perform basic arithmetic operations
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

@app.route('/add', methods=['POST'])
def api_add():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    result = add(x, y)
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def api_subtract():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    result = subtract(x, y)
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def api_multiply():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    result = multiply(x, y)
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def api_divide():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    result = divide(x, y)
    return jsonify({'result': result})



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
   