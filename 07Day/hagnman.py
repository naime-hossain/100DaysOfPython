# TAsk 01 : Randomly select a word from a list of words and ask the user to guess the word,
#  letter by letter. 
# The user has a limited number of attempts to guess the word correctly.
#Check if user has guessed the word correctly or not and display the result accordingly.

import random


words=["python", "java", "javascript", "html", "css", "react", "angular", "nodejs", "django", "flask"]
user_choice=input("choose a word from the list to guess : \n python, java, javascript, html, css, react, angular, nodejs, django, flask \n")
random_word=random.choice(words)
if user_choice==random_word:
    print("You guessed the word correctly!")
else :
    print(f"Sorry, the correct word was '{random_word}'. Better luck next time!")
        