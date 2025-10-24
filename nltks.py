import nltk 
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


text = "NLTK is an excellent and useful library for handling the Python language."


print(word_tokenize(text))
#print statement 1

print(nltk.tokenize.sent_tokenize(text))
#mhmm...interesting print statement here

stopwords = stopwords.words('spanish')
new_text = []
for word in text.split():
    if word not in stopwords:
        new_text.append(word)

print(new_text)
#print statement 3
