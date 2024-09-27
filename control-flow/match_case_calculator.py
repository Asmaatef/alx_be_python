number1 = int(input("Enter the first number"))
number2 =int(input("Enter the second number"))
result = [number1,number2]
operation = str(input(" Choose the operation (+, -, *, /):."))
match result :
  case 1 if operation =="+" :
    result=  sum(number1 + number2)
  case 2 if operation =="-":
    result = number1 - number2
  case 3 if operation == "*":
      result = number1 * number2
  case 4 if operation == "/":
    result = number1 // number2
print("the result is " ,result)