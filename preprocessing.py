# preprocessing.py
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# NLTK'yi başlat
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def preprocess(self, text):
        
        # Küçük harfe dönüştürme
        text = text.lower()
        # Noktalama işaretlerini kaldırma
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])
        # Stopwordleri kaldırma
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word not in self.stop_words]
        # Kelimelerin köklerini bulma
        stemmed_text = [self.stemmer.stem(word) for word in filtered_text]
        return " ".join(stemmed_text)
