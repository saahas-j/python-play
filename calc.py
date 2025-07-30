#python code to perform basic arithmetic operations
from flask import Flask, request, jsonify, render_template_string

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


# Simple HTML UI
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Calculator Web UI</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 400px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; }
        input, select, button { margin: 8px 0; padding: 8px; width: 100%; }
        .result { margin-top: 16px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Calculator</h2>
        <form id="calcForm">
            <input type="number" id="x" placeholder="First number" required step="any">
            <input type="number" id="y" placeholder="Second number" required step="any">
            <select id="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
        <div class="result" id="result"></div>
    </div>
    <script>
        document.getElementById('calcForm').onsubmit = async function(e) {
            e.preventDefault();
            const x = parseFloat(document.getElementById('x').value);
            const y = parseFloat(document.getElementById('y').value);
            const op = document.getElementById('operation').value;
            const resDiv = document.getElementById('result');
            resDiv.textContent = 'Calculating...';
            try {
                const response = await fetch('/' + op, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ x, y })
                });
                const data = await response.json();
                resDiv.textContent = 'Result: ' + data.result;
            } catch (err) {
                resDiv.textContent = 'Error: ' + err;
            }
        };
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
   