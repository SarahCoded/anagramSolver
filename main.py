from flask import Flask, request
from flask import render_template
import requests

from dict_words import oneWord, twoWords, threeWords, fourWords, fiveWords, sixWords, sevenWords, eightWords, nineWords, tenWords, elevenWords, twelveWords, thirteenWords, fourteenWords, fifteenWords, sixteenWords, seventeenWords, eighteenWords, nineteenWords, twentyWords, twentyoneWords

app = Flask(__name__)
if __name__ == "__main__":
    app.run()

def load_words(word_size, jumbledTextSorted):
    if word_size == 5:
        all_valid_words = fiveWords
    elif word_size == 4:
        all_valid_words = fourWords
    elif word_size == 3:
        all_valid_words = threeWords
    elif word_size == 6:
        all_valid_words = sixWords
    elif word_size == 7:
        all_valid_words = sevenWords
    elif word_size == 8:
        all_valid_words = eightWords
    elif word_size == 2:
        all_valid_words = twoWords
    elif word_size == 1:
        all_valid_words = oneWord
    elif word_size == 9:
        all_valid_words = nineWords
    elif word_size == 10:
        all_valid_words = tenWords
    elif word_size == 11:
        all_valid_words = elevenWords
    elif word_size == 12:
        all_valid_words = twelveWords
    elif word_size == 13:
        all_valid_words = thirteenWords
    elif word_size == 14:
        all_valid_words = fourteenWords
    elif word_size == 15:
        all_valid_words = fifteenWords
    elif word_size == 16:
        all_valid_words = sixteenWords
    elif word_size == 17:
        all_valid_words = seventeenWords
    elif word_size == 18:
        all_valid_words = eighteenWords
    elif word_size == 19:
        all_valid_words = nineteenWords
    elif word_size == 20:
        all_valid_words = twentyWords
    elif word_size == 21:
        all_valid_words = twentyoneWords
    # Word size not anagramable, so return empty list
    else:
        return []
    matches = []
    # Loop over the valid words of correct size, and see if they match when both alphabetically sorted
    for word in all_valid_words:
        if ''.join(sorted(word)) == jumbledTextSorted:
            matches.append(word)
    return matches

@app.route("/", methods=['GET', 'POST'])
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
