# Rider height Calculator


# print("Welcome to Rider height checker \n")
# height=float(input("What is your Height in CM ? : cm \n "))
# if height >=120 :
#     print("You can Ride the roller coaster")
# elif height <120 :
#     print("Sorry you cant Ride the roller coaster")




# Odd pr even checker

# print("Welcome to odd or even checker \n")
# number=float(input("Write the number you want to check ? : \n"))

# if number%2==0 : 
#     print("This number is even")
# else : 
#     print("This number is odd")





# Roller coaster with age and height checker
# print("Welcome to Roller Coaster Ride \n")
# height=float(input("what is your height in cm ? : \n"))
# if height >=120 :
#     print("You can Ride the roller coaster \n")
#     age=int(input("What is your age ? : \n"))
#     if age <12 :
#         print("please Pay $5")
#     elif age>=12 and age <=18 :
#         print ("Please Pay $7" )
#     else : 
#         print("Please Pay $12")
# else : 
#     print("Sorry you cant Ride the roller coaster") 
# 
# 
# 
# 




# 
#  
# 
# BMI Calculator with Interpretations
# Add some if/elif/else statements to the
#  BMI calculator so that 
# it interprets the BMI values calculated.

# If the bmi is under 18.5 (not including), 
# print out "underweight"

# If the bmi is between 18.5 (including) and 25 
# (not including), print out "normal weight"

# If the bmi is 25 (including) or over, 
# print out "overweight"
#       
# 
# 



# print("Welcome to BMI Calculator \n")
# height=float(input("What is you Height in M ? \n"))
# weight=float(input("What is your weight in KG ? \n"))
# BMI=weight/height**2
# if BMI<18.5 :
#     print(f"Your BMI is {BMI} and you are underweight")
# elif BMI>=18.5 and BMI<25 :
#     print (f"Your BMI is {BMI} and you are normal Weight")
# # elif BMI >=25 :
# else :
#     print (f"Your BMI is {BMI} and you are overweight")


# Roller Coaster with extra photos and bill checker

# print("Welcome to Roller Coaster Ride")
# height=float(input("What is your Height in CM ? \n"))
# if height > 120 :
#     age = float(input("What is your Age ? \n"))
#     if age <12 :
#       payable= 5
#       print("Pay $5 for Ride")
#     elif age >=12 and age <=18 :
#       payable = 7
#       print("Pay $7 for the Ride")
#     else :
#       payable = 12
#       print("Pay 12$ for the ride")
#     want_photos = input("Want photos for extra $3 ? Type yes or no ").lower()
#     if want_photos == "yes" :
#       payable += 3
#       print(f"Your Total bill is {payable}")
#     else :
#       print(f"Your total bill is {payable}")  
    

# else :
#   print ("You can not Ride")


# pizza order place


# print("Welcome to Pizzarela")
# size = input("What size do You want ? S , M or L \n")
# peporoni =input("Do you want Peporoni ? Type Y or N \n")
# extra_cheese = input("Do you want Extra Cheese ? Type Y or N \n")
# pizza_price = 0
# if size == "S" :
#   pizza_price = 20
# elif size == "M" :
#   pizza_price = 25
# else :
#   pizza_price = 30
# if peporoni  == "Y" :
#    if size == "S" :
#      pizza_price += 2
#    else :
#      pizza_price += 3
# if extra_cheese == "Y" :
#   pizza_price += 1
# print(f"Your total bill is ${pizza_price} Thank you" ) 
# 
# 
# 
#


#Roller coaster with age,photos and midlife-crisis



print("Welcome to roller coaster Ride")
height=float(input("Enter your Height in CM : \n"))
total_ride_price = 0
if height > 120 :
  #can ride block
  age = int(input("What is your Age ? : \n"))
  if age< 12 :
    total_ride_price += 5
  elif age <=12 and age < 18 :
    total_ride_price += 7
  elif age>=45 and  age <=55  :
    total_ride_price = 0
    print("You are in Midlife crisis and you dont need to pay anything ") 
  else :
    total_ride_price += 12
  
  want_photos = input("Want to take photo ? Type Y or N : \n")
  if want_photos == "Y" :
    total_ride_price += 3
    print(f"You need to pay ${total_ride_price} for the ride . thanks ")
  else :
    print(f"You need to pay ${total_ride_price} for the ride . thanks ")  
     
        

else :
  print("Sorry you cant Ride")



