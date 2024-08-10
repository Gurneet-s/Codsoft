# CALCULATOR

print("Welcome to the calculator")

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter your choice (1/2/3/4): "))

if choice == 1:
  result = num1 + num2
  print("Result:",result)
elif choice == 2:
  result = num1 - num2
  print("Result:",result)
elif choice == 3:
  result = num1 * num2
  print("Result:",result)
elif choice == 4:
  if num2!= 0:
    result = num1 / num2
    print("Result:",result)
  else:
    print("Error: Division by zero!")
else:
  print("Invalid input")