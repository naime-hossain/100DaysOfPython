# BMI Calculator
print("Wlcome to BMI Claculator \n")
bmi_lower_limit=18.5
bmi_upper_limit=24.9
weight=float(input("Enter your weight in kg : \n"))
height=float(input("Enter your Height in meter : \n"))
bmi=weight/(height**2)
if bmi< bmi_lower_limit :
    print("Your BMI is :" +  str(bmi)+ "Which is underwight , Eat more")
elif bmi>bmi_upper_limit :
    print("Your BMI is " +str(bmi)+ "which is overweight , Eat less and excercise more ")

else : print("Your BMI is "+str(bmi)+" 45Which is Normal, Keep it up")