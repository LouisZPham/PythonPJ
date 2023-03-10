from nltk.tokenize import word_tokenize

# Define a list of words that typically start a question
question_words = ["what", "why", "when", "where", 
             "name", "is", "how", "do", "does", 
             "which", "are", "could", "would", 
             "should", "has", "have", "whom", "whose", "don't"]

question = input("Input a sentence: ")
# Convert the input sentence to lowercase
question = question.lower()
# Tokenize the sentence into a list of words
question = word_tokenize(question)
# Check if the first word in the list is one of the question words
if any(x in question[0] for x in question_words):
    print("This is a question!")
else:
    print("This is not a question!")