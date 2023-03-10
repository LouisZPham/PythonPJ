from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a Word or words : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)