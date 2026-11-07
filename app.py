from flask import Flask, jsonify, render_template, request
from calculator_pkg import add, subtract, multiply, divide

app = Flask(__name__)

OPERATIONS = {
    "add": ("+", add),
    "subtract": ("−", subtract),
    "multiply": ("×", multiply),
    "divide": ("÷", divide),
}


def calculate(a_value, b_value, op_key):
    if op_key not in OPERATIONS:
        raise KeyError(f"Unsupported operation: {op_key}")

    _, func = OPERATIONS[op_key]
    return func(float(a_value), float(b_value))


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
            result = calculate(a, b, op_key)
        except ValueError:
            error = "Please enter valid numbers."
        except ZeroDivisionError:
            error = "Division by zero is not allowed."
        except KeyError:
            error = "Unsupported operation selected."
        except Exception as exc:
            error = f"Unexpected error: {exc}"
    return render_template("index.html", result=result, error=error, a=a, b=b, op_key=op_key, operations=OPERATIONS)


@app.route("/api/calculate", methods=["POST"])
def calculate_api():
    payload = request.get_json(silent=True) or request.form
    a = payload.get("a", "")
    b = payload.get("b", "")
    op_key = payload.get("operation", "add")

    try:
        result = calculate(a, b, op_key)
        return jsonify({"result": result, "operation": op_key, "symbol": OPERATIONS[op_key][0]})
    except ValueError:
        return jsonify({"error": "Please enter valid numbers."}), 400
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero is not allowed."}), 400
    except KeyError:
        return jsonify({"error": "Unsupported operation selected."}), 400
    except Exception as exc:
        return jsonify({"error": f"Unexpected error: {exc}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
