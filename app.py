from flask import Flask, render_template, request
from calculator_pkg import add, subtract, multiply, divide

app = Flask(__name__)

OPERATIONS = {
    "add": ("+", add),
    "subtract": ("−", subtract),
    "multiply": ("×", multiply),
    "divide": ("÷", divide),
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    a = ""
    b = ""
    op_key = "add"
    if request.method == "POST":
        a = request.form.get("a", "").strip()
        b = request.form.get("b", "").strip()
        op_key = request.form.get("operation", "add")
        try:
            a_val = float(a)
            b_val = float(b)
            _, func = OPERATIONS[op_key]
            result = func(a_val, b_val)
        except ValueError:
            error = "Please enter valid numbers."
        except ZeroDivisionError:
            error = "Division by zero is not allowed."
        except Exception as exc:
            error = f"Unexpected error: {exc}"
    return render_template("index.html", result=result, error=error, a=a, b=b, op_key=op_key, operations=OPERATIONS)


if __name__ == "__main__":
    app.run(debug=True)
