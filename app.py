import math
operations_list = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo", "Raising to a power", "Square root", "Logarithm", "Sine", "Cosine", "Tangent"]

while True:
  user_input = print("\nChoose the math operation. \n\n" + "".join(["{} - {}\n".format(idx, ele) for (idx, ele) in enumerate(operations_list)]))
  user_input = input("Your option from the menu: ")
  # Addition
  if user_input == "0":
    first_value = float(input("\nFirst value: "))
    second_value = float(input("\nSecond value: "))
    print("\nThe result is: " + str(first_value + second_value))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Subtraction
  elif user_input == "1":
    first_value = float(input("\nFirst value: "))
    second_value = float(input("\nSecond value: "))
    print("\nThe result is: " + str(first_value - second_value))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Multiplication
  elif user_input == "2":
    first_value = float(input("\nFirst value: "))
    second_value = float(input("\nSecond value: "))
    print("\nThe result is: " + str(first_value * second_value))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Division
  elif user_input == "3":
    first_value = float(input("\nFirst value: "))
    second_value = float(input("\nSecond value: "))
    print("\nThe result is: " + str(first_value / second_value))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Modulo
  elif user_input == "4":
    first_value = float(input("\nFirst value: "))
    second_value = float(input("\nSecond value: "))
    print("\nThe result is: " + str(first_value % second_value))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Raising to a power
  elif user_input == "5":
    first_value = float(input("\nFirst value: "))
    second_value = float(input("\nSecond value: "))
    print("\nThe result is: " + str(math.pow(first_value, second_value)))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Square root
  elif user_input == "6":
    value = float(input("\nEnter value to square root: "))
    print("\nThe result is: " + str(math.sqrt(value)))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Logarithm
  elif user_input == "7":
    value = float(input("\nEnter value for Logarithm (base 2): "))
    print("\nThe result is: " + str(math.log(value, 2)))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Sine
  elif user_input == "8":
    value = float(input("\nEnter value in degrees for sine: "))
    print("\nThe result is: " + str(math.sin(math.radians(value))))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Cosine
  elif user_input == "9":
    value = float(input("\nEnter value in degrees for cosine: "))
    print("\nThe result is: " + str(math.cos(math.radians(value))))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  # Tangent
  elif user_input == "10":
    value = float(input("\nEnter value in degrees for tangent: "))
    print("\nThe result is: " + str(math.tan(math.radians(value))))

    back = input("\nGo back to the main menu? (y/n) ")

    if back == "y":
      continue
    else:
      break
  
  else:
    print("\nInvalid Option")
    continue

# End of Program