from flask import Flask, request, jsonify
from tool import fetch_stock_data

app = Flask(__name__)

@app.route("/get_stock", methods=["GET"])
def get_stock():
    ticker = request.args.get("ticker", "").upper()
    if not ticker:
        return jsonify({"error": "Ticker symbol required"}), 400
    
    response = fetch_stock_data(ticker)
    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
