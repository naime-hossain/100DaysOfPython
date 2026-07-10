# TAsk 01 : Randomly select a word from a list of words and ask the user to guess the word,
#  letter by letter. 
# The user has a limited number of attempts to guess the letter of the word correctly.
#Check if user has guessed the word correctly or not and display the result accordingly.

import random


words=["python", "java", "javascript", "html", "css", "react", "angular", "nodejs", "django", "flask"]
user_choice=input("choose a letter  to guess : \n").lower()
random_word=random.choice(words)
random_word=random_word.lower()
random_word_array=list(random_word)

print(random_word)

for i in random_word_array :
    if user_choice == i :
        print("Right")
    else :
        print("Wrong")    

# if user_choice==random_word:
#     print("You guessed the word correctly!")
# else :
#     print(f"Sorry, the correct word was '{random_word}'. Better luck next time!")
