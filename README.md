# Anagram Solver

A fast, lightweight anagram solver. Deployed on PythonAnywhere. It can be accessed at [https://sarahcoded.pythonanywhere.com](https://sarahcoded.pythonanywhere.com)

## Contents
- [Installation](#Installation)
- [Searching Algorithm](#Searching-Algorithm)
- [Definition Lookup](#Definition-Lookup)
- [Word List](#Word-List)
- [Design](#Design)
- [Testing](#Testing)

### <a name="Installation"></a>Installation
To access this project locally, run the following from your terminal

Clone the repo and cd into it
```
git clone https://github.com/SarahCoded/anagramSolver.git
cd anagramSolver
```

Create a virtual environment to install packages

Windows 
```
py -3 -m venv venv 
venv\Scripts\activate
```

Mac/Linux
```
python3 -m venv venv
. venv/bin/activate
```

Install the requirements
```
pip install -r requirements.txt
```
Name the app main
```
export FLASK_APP=main.py
```
Run flask locally on your browser
```
flask run
```

### <a name="Searching-Algorithm"></a>Searching algorithm
The anagrams are found using a Python dictionary, which are faster at searching in comparison to lists. In order to optimise anagram searching, I have created a python file wordlist.py, which contains a single dictionary, with the key being the word, and the value being the length of the word. If the letters the user has provided are too long or short, searching is skipped and an empty list will be returned. Else, the dictionary will be searched, and if a valid word from the dictionary is the same size as the letters the user has given, both sets of letters will be sorted alphabetically to see if there is a match. If there is, the corresponding valid word from the dictionary will be added to the matches list. Once the dictionary has been searched, the matches will be returned. For example, if the user inputs the letters 'tras', it will be sorted to 'arst', and the matches will be ['arts', 'rats', 'star', 'tars', 'tsar'], because when sorted, all these valid words equalled 'arst'. 

### <a name="Definition-Lookup"></a>Definition Lookup

I have implemented a lookup function using an API call from [https://dictionaryapi.dev/](https://dictionaryapi.dev/). Initially, I wanted all of the word definitions to appear along with the results, however I soon realised this would not be possible unless I was either willing to sacrifice loading time as an API call was requested however many times for each word, or if I set up a SQL database instead which contained all the definitions. 

As a compromise, because I had already implemented the anagram lookup and was pleased with how quick it had become, I decided to make the API call optional, so it would only be called if the user wants to know the definition. I implemented the call client side using the async function in JavaScript. It takes a couple of seconds to load up each definition, but it is better than nothing. If the API fails to load, or there isn't a matching word, the error will be caught and 'Definition not found' will be displayed instead. 

### <a name="Word-List"></a>Word List

Estimates of how many words are in the English language range from around 170,000 to 520,000. In order to implement the solver, I looked about for a suitable .txt file that would contain a reasonable amount of valid words. Initially, I went for a list on the higher end of the spectrum, but I realised that it would take longer to search through to find matches, and it would also give obscure words that would not match up to the API call to look up the definition. In the end, I went with a smaller word list of only 84,000 words from [http://www.gwicks.net/dictionaries.htm](http://www.gwicks.net/dictionaries.htm). In the future, I hope to switch to a larger word list that is closer aligned to the API call's word list, because a definition is not found on a small number of obscure words, which ironically, would be words a user would be more inclined to know the definition for!

In order to convert the .txt file into a Python dictionary, I used Python's built in file writing to transform aa into "aa": 2, etc. in the .txt file. Then, I converted the .txt file into a .py file and added the necessary {} and variable naming to turn it into a Python dictionary, ready to be imported into main.py. 

### <a name="Design"></a>Design
I have intended for the app to have a 
minimalist design. This is so that it will load reasonably quickly, even if you have limited internet connectivity. Initially, I had included the Bootstrap library, so that I wouldn't need to do as much CSS. However, after noticing how large their CSS files were, I decided to do the CSS myself, looking online at the Bootstrap source code for inspiration.

### <a name="Testing"></a>Testing
Basic testing has been implemented for this application using pytest. Currently, 15 tests have been written with a 100% pass rate. I have separated testing into four files, which cover the API call to get the word definition, live server testing on PythonAnywhere, the load_word function to source anagrams, and path testing on Flask. 
