from flask import Flask, render_template, request, jsonify
from conversions import convert

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def converter():
    data = request.get_json()

    category = data.get("category")
    from_unit = data.get("from")
    to_unit = data.get("to")
    value = data.get("value")

    try:
        value = float(value)
    except (ValueError, TypeError):
        return jsonify({
            "success": False,
            "message": "Please enter a valid number."
        })

    try:
        result = convert(category, from_unit, to_unit, value)

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)