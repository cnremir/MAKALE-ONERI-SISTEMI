from flask import Flask, request, session, render_template, g
from fasttext_processing import FastTextProcessor
from scibert_processing import SciBERTProcessor
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
data_path = "./Inspec/docsutf8"

fasttext_processor = None
scibert_processor = None

@app.before_request
def initialize_processors():
    global fasttext_processor, scibert_processor
    fasttext_processor = FastTextProcessor(data_path, [])
    scibert_processor = SciBERTProcessor(data_path, [])

@app.route('/')
def index():
    return render_template('ss.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_interests = request.form.getlist('interests')
    print("user interests:", user_interests)
    session['user_interests'] = user_interests

    global fasttext_processor, scibert_processor

    fasttext_recommendations = fasttext_processor.recommend_articles(user_interests)
    scibert_recommendations = scibert_processor.recommend_articles(user_interests)

    return render_template('recommendations.html', fasttext_recommendations=fasttext_recommendations, scibert_recommendations=scibert_recommendations)

@app.route('/feedback', methods=['POST'])
def feedback():
    liked_article_ids = request.form.get('liked_ids')
    liked_article_ids = [int(id) for id in liked_article_ids.split(',')]
    print(liked_article_ids)
    global fasttext_processor, scibert_processor

    fasttext_feedback_recommendations = fasttext_processor.recommend_feedback_articles(liked_article_ids)
    scibert_feedback_recommendations = scibert_processor.recommend_feedback_articles(liked_article_ids)

    return render_template('feedback_recommendations.html', fasttext_feedback_recommendations=fasttext_feedback_recommendations, scibert_feedback_recommendations=scibert_feedback_recommendations)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)