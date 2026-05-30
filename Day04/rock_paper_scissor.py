#rock paper scissor game

import random

rock = '''

          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
'''
paper = '''
         _______
      ---'   ____)____
                ______)
                _______)
                _______)
      ---.__________)
'''
scissors='''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)

      '''
choices={"r":rock,"p":paper,"s":scissors}
user_choice = input("what is your choice Rock, paper or scissor ? Type r,p or s ").lower()
computer_choice = random.choice(list(choices.keys()))
if user_choice == "r" :
    print (f"User selected Rock : n\ {rock}")
elif user_choice == "p" :
       print (f"User selected Paper : n\ {paper}")
else :
      print (f"User selected scissors : n\ {scissors}") 
print (f"Computer selected  : n\ {choices[computer_choice]}")             

# Rock crushes Scissors: Rock wins.
# Scissors cuts Paper: Scissors win.
# Paper covers Rock: Paper wins.

# Rock > scissors , scissors > paper , paper > rock 

if computer_choice == user_choice :
      print("Its a tie")
else :
        
    if computer_choice == "r" :
        if user_choice == "s" :
            print("Computer Win")
        if user_choice == "p":
            print("You win")


    if computer_choice == "s" :
        if user_choice == "r" :
            print("You Win")
        if user_choice == "p":
            print("You win")


    if computer_choice == "p" :
        if user_choice == "r" :
            print("Computer Win")
        if user_choice == "s":
            print("You win")                  

        


