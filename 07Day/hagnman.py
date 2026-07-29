# TAsk 01 : Randomly select a word from a list of words and ask the user to guess the word,
#  letter by letter. 
# The user has a limited number of attempts to guess the letter of the word correctly.
#Check if user has guessed the word correctly or not and display the result accordingly.

import random


words=["python", "java", "javascript", "html", "css", "react", "angular", "nodejs", "django", "flask"]

random_word=random.choice(words)
random_word=random_word.lower()
random_word_array=list(random_word)

print(random_word)
dummy=""
for i in random_word_array :
    dummy+="_"
print(dummy)  
display=""
user_choice=input("choose a letter  to guess : \n").lower()
for i in random_word_array :

    if user_choice == i :
               
               
        # print("Right")
               display+=i
               
        #
    else :
         display+="_"
        # print("Wrong") 
        #    
print(f"Your guess is : {display}")


