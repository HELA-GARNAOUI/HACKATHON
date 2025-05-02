from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_keywords(text):
    return text.lower()

def compute_similarity(job_text, cv_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([job_text, cv_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    
    job_words = set(job_text.lower().split())
    cv_words = set(cv_text.lower().split())
    matched_keywords = list(job_words & cv_words)

    return score, matched_keywords
