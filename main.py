
num1 = float(input("Hey! Welcome to Victor's Calculator. Enter the first number: "))
op = input("Enter * , + , / , or - :")
num2 = float(input("Enter another number: "))

if op == "+": 
  print(num1 + num2)
elif op == "*":
  print(num1 * num2)
elif op == "/":
  print(num1 / num2)
elif op == "-":
  print(num1 - num2)
else:
  print("Hmm... I don't know that operator.")

