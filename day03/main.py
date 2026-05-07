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
print("Welcome to BMI Calculator \n")
height=float(input("What is you Height in M ? \n"))
weight=float(input("What is your weight in KG ? \n"))
BMI=weight/height**2
if BMI<18.5 :
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI>=18.5 and BMI<25 :
    print (f"Your BMI is {BMI} and you are normal Weight")
# elif BMI >=25 :
else :
    print (f"Your BMI is {BMI} and you are overweight")


             