import math
operations_list = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo", "Raising to a power", "Square root", "Logarithm", "Sine", "Cosine", "Tangent"]

def calculate(user_input, v1, v2):
  operation = operations_list[user_input]
  if (operation == "Addition"):
    return v1 + v2
  elif (operation == "Subtraction"):
    return v1 - v2
  elif (operation == "Multiplication"):
    return v1 * v2
  elif (operation == "Division"):
    return v1 / v2
  elif (operation == "Modulo"):
    return v1 % v2
  elif (operation == "Raising to a power"):
    return pow(v1, v2)
  elif (operation == "Square root"):
    return math.sqrt(v1)
  elif (operation == "Logarithm"):
    return math.log(v1)
  elif (operation == "Sine"):
    return math.sin(v1)
  elif (operation == "Cosine"):
    return math.cos(v1)
  elif (operation == "Tangent"):
    return math.tan(v1)

def start_main_menu():
  user_input = input("Choose the math operation. \n\n" + "".join(["{} - {}\n".format(idx, ele) for (idx, ele) in enumerate(operations_list)]) + "\n")
  if int(user_input) in range(11):
    first_value = 0
    second_value = 0
    if (int(user_input) in range(6)):
      first_value = float(input("First value: "))
      second_value = float(input("Second value: "))
    else:
      first_value = float(input("Value: "))
    result = calculate(int(user_input), v1=first_value, v2=second_value)

    print(f"The result is {result}")

    choice = input("Go back to the main menu? (y/n) ")
    if (choice == "y"): start_main_menu()
  else:
    print("Invalid Option")
    start_main_menu()



start_main_menu()




