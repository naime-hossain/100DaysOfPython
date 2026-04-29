# final project for day 2 
print("Welcome to Tip Calculator \n")
total_bill= float(input("what was total bill ? : \n"))
tip_percentage=float(input("what is the Percentage ? 10,15,20, or 30 ? : \n"))
number_of_people=float(input("how many people will share the bill ? : \n"))
tip_amount=total_bill*tip_percentage/100
total_bill_per_person_with_tip=float((total_bill+tip_amount)/number_of_people)
print("Each person should pay : " + str(total_bill_per_person_with_tip))
