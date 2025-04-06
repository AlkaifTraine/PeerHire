from flask import Flask, request, jsonify
from model import recommend_freelancers

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    job_desc = data.get("description")
    budget = data.get("budget")

    if not job_desc or not budget:
        return jsonify({"error": "Missing job description or budget"}), 400

    recommendations = recommend_freelancers(job_desc, budget)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
