# python-play

## Calculator Web App Features

- **Modern Web Calculator UI**
  - Responsive, visually appealing design with a green gradient background.
  - Calculator display at the top shows the full expression as you type and the result after calculation.
  - On-screen number and operator keyboard for input (digits, decimal, +, −, ×, ÷, clear, equals).
  - You can also type the full expression directly into the display using your physical keyboard.
  - Press Enter or click `=` to calculate.

- **Backend with Flask API**
  - All calculations are performed by a Python Flask backend.
  - Supports addition, subtraction, multiplication, and division.
  - AJAX requests are sent to the backend for each calculation.

- **3D Animated Background**
  - Uses Three.js for a smooth, animated 3D background.

- **Other Details**
  - Result is always shown at the top in the display box.
  - Only valid calculator characters are accepted in the display.
  - Clear (`C`) button resets the calculator.

---

To run the app:
1. Install requirements: `pip install flask`
2. Run: `python calc.py`
3. Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
