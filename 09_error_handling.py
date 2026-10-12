try:
number = int(input(“Enter a number: “))
result = 100 / number
print(“Result:”, result)

except ValueError:
print(“Error: Please enter a valid number.”)

except ZeroDivisionError:
print(“Error: Cannot divide by zero.”)
