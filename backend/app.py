from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from matcher.parser import extract_text
from matcher.nlp import extract_keywords, compute_similarity

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/match', methods=['POST'])
def match_cvs():
    job_file = request.files.get('job')
    cv_files = request.files.getlist('cvs')

    if not job_file or not cv_files:
        return jsonify({"error": "Missing job file or CVs"}), 400

    job_text = extract_text(job_file)
    job_keywords = extract_keywords(job_text)

    results = []
    for cv_file in cv_files:
        cv_text = extract_text(cv_file)
        score, matched_keywords = compute_similarity(job_keywords, cv_text)
        results.append({
            "filename": cv_file.filename,
            "score": round(score * 100, 2),
            "matched_keywords": matched_keywords
        })

    results.sort(key=lambda x: x['score'], reverse=True)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
