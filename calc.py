def calculate(num1, num2, operator):
  try:
    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      if num2 == 0:
        raise ZeroDivisionError("Division by zero")
      else:
        result = num1 / num2
    else:
      raise ValueError("Invalid operator")
    return result
  except ZeroDivisionError as e:
    return str(e)
  except ValueError as e:
    return str(e)

def main():
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operator = input("Enter the operator (+, -, *, /): ")

      result = calculate(num1, num2, operator)
      print(f"{num1} {operator} {num2} = {result}")
      break
    except ValueError:
      print("Incorrect value. Please enter a number.")

if __name__ == "__main__":
  main()