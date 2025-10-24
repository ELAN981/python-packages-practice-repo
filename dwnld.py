
# import nltk
# try:
#     nltk.download('punkt_tab')
#     nltk.download('stopwords')
#     print("Download successful!")
# except Exception as e:
#     print(f"An error occured: {e}")

import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

# Example text
text = "This is an example sentence for tokenization."

# Tokenize the text
tokens = word_tokenize(text)
print("Tokens:", tokens)

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

text = "This is a test. Let's see how it works."
print(sent_tokenize(text))  # Should work fine

