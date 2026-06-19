# We will build a simple calculator where the user can input two numbers
# and the operator they want to use and the calculator will show result of the calculation.
print("Welcome to Python calculator Project")
first_number= float(input("Type your first number : \n"))
second_number = float(input("What is your second Number ? : \n"))
operator = input("Choose an operator tpye : *,/,+ or - : \n")
result = 0;
if operator == "+" :
  result = first_number+second_number
elif operator == "-" :
  result = first_number-second_number 
elif operator == "*" : 
  result = first_number*second_number
elif operator == "/":
  result = first_number/second_number
else :
  print ("Please Type a valid Operator")      

print(f"The result is {result}")