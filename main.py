import messages
import read
import operations

messages.welcomeMessage()

while True:
  try:  
    land_data = read.readDataFromFile("Rental Data.txt")
    read.displayTable(land_data)
    print("Enter '1' to rent a land: ")
    print("Enter '2' to return land: ")
    print("Enter '3' to exit: ")
    choice = int(input("Please enter a value: "))
    if choice == 1:
        print("You will now rent a land\n")
        name = input("Enter your name: ")
        landId = int(input("Enter the Land ID of the land you want to rent: "))
        operations.rentLand(name, landId)
    elif choice == 2:
        print("You will now return a land\n")
        name = input("Enter you name: ")
        operations.returnLand(name)
    elif choice == 3:
        messages.thankYouMessage()
        break
    else:
        messages.plusLines("Enter a valid input")
  except ValueError:
     print("Invalid input, please enter a integer number")
