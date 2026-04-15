from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open("data/customers.json") as f:
    customers = json.load(f)

@app.route("/api/health")
def health():
    """
    Simple health check endpoint to verify the server is running.
    """
    return {"status": "ok"}

@app.route("/api/customers")
def get_customers():
    """
    Fetch paginated list of customers. Accepts 'page' and 'limit' as query parameters for pagination.
     If not provided, defaults to page=1 and limit=10.
    """
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": customers[start:end],
        "total": len(customers),
        "page": page,
        "limit": limit
    })

@app.route("/api/customers/<id>")
def get_customer(id):
    """
    Fetch a single customer by ID. If not found, return 404.
    """

    for c in customers:
        if c["customer_id"] == id:
            return jsonify(c)
    return jsonify({"error": "Customer not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)