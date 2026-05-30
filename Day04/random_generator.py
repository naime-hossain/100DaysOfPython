import random
friends = ["Shoshi","Madhubi","Nafiyan","Faiyad","Rukaiya","Bhuiyan"]
countries = ["Newzealand","UK","USA","Denmark","Spain","Austria"]

# Now print random person
print(f"You are {random.choice(friends)} and your destination is {random.choice(countries)}")
# Random number within a range
random_number_0_to_1 = random.randint(1,10)
print(f"How much this will good for you(0 to 10 ): {random_number_0_to_1}")

#Random FLoat number 0 to 1 (if multiply by 10,20,or any number this will work)
random_floating_number = random.random() * 100;
print(f"Your Probability if Going there (in %): {random_floating_number}")

#Uniform floating random number , random float but with range 
random_uniform_float_number = random.uniform(1,100)
print(f"Your Probability of not going there : {random_uniform_float_number}")


#Head or Tails Game 
choices = ["Head","Tails"]
result = random.choice(choices)
print (f"You get {result}")

#using random number
random_number = random.randint(0,1)
if random_number == 0 :
  print ("You get Head")

else :
  print ("You get Tails")

#lets make it more playful
user_choice =input("what is your choice? Head(Type h) or Tails(Type T)  \n").lower()
if random_number == 0 and user_choice == "h" :
  print("You Select Head and  win the toss")
elif random_number == 1 and user_choice == "t" :
  print (" You Selected Tail and win the toss")  
else :
  print(f" You slelcted {user_choice} Lost the toss") 