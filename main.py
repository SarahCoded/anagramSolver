from flask import Flask, request, render_template
from wordlist import words
import requests

app = Flask(__name__)
if __name__ == "__main__":
    app.run()

def load_words(word_size, jumbledTextSorted):
    matches = []
    for k, v in words.items():
        if v == word_size:
            if ''.join(sorted(k)) == jumbledTextSorted:
                matches.append(k)
    return matches

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def anagramsubmit():
    if request.method == 'POST':
        jumbledText = request.form.get('anagram').lower()
        
        # Avoid scripting attacks
        if not jumbledText.isalpha():
            return render_template('index.html')
        
        # Get valid words of matching length and letters
        valid_answers = load_words(len(jumbledText), ''.join(sorted(jumbledText)))
        
    return render_template('submit.html', valid_answers=valid_answers)
