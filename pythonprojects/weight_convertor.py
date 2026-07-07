# User will Enter their weight and unit (Kgs or LBS) 
#Then we will convert the weight 
# to the unit that user did not enter 
# 1 Kgs = (1 * 2.205)lbs
# 1 LBS = (1/2.205)kgs
# 
#  

weight = int(input("Enter your Weight \n"))
unit = input("What is the unit ? Type K for Kgs or L for Pounds \n ")

if unit == "K":
    weight=weight*2.205
    unit="Lbs"
elif unit == "L":
    weight=weight/2.205
    unit = "Kgs"
else :
    print(f"{unit} is not a valid Weight unit")
print(f"Your weight is {weight}{unit}")    
