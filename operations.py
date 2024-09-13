import read
import messages
import write
import datetime

rentalFullDate = 0

def rentLand(name, landId):
    """
    Handles the process of renting land, including validation and updating land availability.

    Args:
        name (str): The name of the customer renting the land.
        landId (int): The ID of the land to rent.
    """
    try:
        land_data = read.readDataFromFile("Rental Data.txt")
        landList = []
        rentalTimeList = []

        landRent = True

        while landRent:
            if landId < 1 or landId > len(land_data):
                messages.plusLines("Invalid Land ID!! Please enter a valid Land ID.")
                landId = int(input("Enter the Land ID of the land you want to rent: "))
            else:
                if land_data[landId][5] == "Available":
                    if landId not in landList:
                        rentalTime = int(input("How long do you want to rent the land? "))
                        landList.append(landId)
                        rentalTimeList.append(rentalTime)
                        write.changeLandAvailability(landId)
                    else:
                        messages.plusLines("You just rented this land. Please rent other lands if any.")
                else:
                    messages.plusLines("Sorry, the land you want to rent is not available. Please select an available land if any.")
                    landId = int(input("Enter the Land ID of the land you want to rent: "))
                validDecision = False
                while not validDecision:
                    decision = input("Do you want to rent more lands that are available? (Y/N): ")
                    if decision.lower() == "n":
                        validDecision = True
                        landRent = False
                    elif decision.lower() == "y":
                        landId = int(input("Enter the Land ID of the land you want to rent: "))
                        validDecision = True
                    else:
                        messages.plusLines("Invalid entry!! Please enter a valid input.")
                        validDecision = False

        rentInvoice(name, landList, rentalTimeList)
    except Exception as e:
        messages.plusLines("An error occurred: " + str(e))

def rentInvoice(name, landList, rentalTimeList):
    """
    Generates and prints the rental invoice for the rented lands.

    Args:
        name (str): The name of the customer.
        landList (list): List of land IDs rented.
        rentalTimeList (list): List of rental times for each land ID.
    """
    try:
        rentalFullDate = datetime.datetime.now()
        rentalDate = str(rentalFullDate.year) + "-" + str(rentalFullDate.month) + "-" + str(rentalFullDate.day)
        messages.plusLines("Land Rental Bill Invoice")
        rent = totalRent(landList, rentalTimeList)
        land_data = read.readDataFromFile("Rental Data.txt")
        for key, value in land_data.items():
            for i in range(len(landList)):
                if key == landList[i]:
                    messages.dashes()
                    print("Name of the rental customer:", name)
                    print("Land ID:", key)
                    print("Kitta No.:", value[0])
                    print("City/District Name:", value[1])
                    print("Direction the land is facing:", value[2])
                    print("Anna:", value[3])
                    print("Price per Anna per month:", value[4])
                    print("Land Rental Time:", rentalTimeList[i])
                    print("Total price of Land ID No.", key, ":", rent[0][i])
                    print("Day of Land Rental:", rentalDate)
                    messages.dashes()
        messages.dashes()
        print("Total Price of", len(landList), "land:", rent[1])
        messages.dashes()
        write.storeRentInvoiceData(name, landList, rentalTimeList)
    except Exception as e:
        messages.plusLines("An error occurred: " + str(e))

def totalRent(landList, rentalTimeList):
    """
    Calculates the total rent for the rented lands.

    Args:
        landList (list): List of land IDs rented.
        rentalTimeList (list): List of rental times for each land ID.

    Returns:
        tuple: A tuple containing a list of rents for each land ID and the total rent.
    """
    try:
        rent = []
        totalRent = 0
        land_data = read.readDataFromFile("Rental Data.txt")
        for key, value in land_data.items():
            for i in range(len(landList)):
                if key == landList[i]:
                    rent.append(value[3] * value[4] * rentalTimeList[i])
                    totalRent += rent[-1]  # Use -1 to access the last element in total
        return rent, totalRent
    except Exception as e:
        messages.plusLines("An error occurred: " + str(e))
        return [], 0

def totalReturningRent(landList, rentalTime, returnTime):
    """
    Calculates the total rent including fines for returning land after the rental period.

    Args:
        landList (list): List of land IDs being returned.
        rentalTime (int): The initial rental time.
        returnTime (int): The time when the land is returned.

    Returns:
        tuple: A tuple containing the total rent, fine, exceeded months, and return time.
    """
    try:
        totalRent = 0
        fine = 0
        land_data = read.readDataFromFile("Rental Data.txt")
        for key, value in land_data.items():
            if key in landList:
                exceededMonth = returnTime - rentalTime
                if exceededMonth > 0:
                    fine = exceededMonth * 0.1 * value[4]
                totalRent = returnTime * value[4] + fine
        return totalRent, fine, exceededMonth, returnTime
    except Exception as e:
        messages.plusLines("An error occurred: " + str(e))
        return 0, 0, 0, 0

def returnInvoice(name, landList, rentalTime, returnTime):
    """
    Generates and prints the return invoice for the returned lands.

    Args:
        name (str): The name of the customer.
        landList (list): List of land IDs being returned.
        rentalTime (int): The initial rental time.
        returnTime (int): The time when the land is returned.
    """
    try:
        returnFullDate = datetime.datetime.now()
        returnDateList = []
        messages.plusLines("Land Return Bill Invoice")
        land_data = read.readDataFromFile("Rental Data.txt")
        for key, value in land_data.items():
            for i in range(len(landList)):
                rent = totalReturningRent(landList, rentalTime, returnTime)
                returnDate = str(returnFullDate.year) + "-" + str(returnFullDate.month) + "-" + str(returnFullDate.day)
                returnDateList.append(returnDate)
                if key == landList[i]:
                    messages.dashes()
                    print("Name of the rental customer:", name)
                    print("Land ID:", key)
                    print("Kitta No.:", value[0])
                    print("City/District Name:", value[1])
                    print("Direction the land is facing:", value[2])
                    print("Anna:", value[3])
                    print("Price per Anna per month:", value[4])
                    print("Land Rental Time:", returnTime)
                    print("Day of Land Return:", returnDate)
                    print("Total price of Land ID No.", key, ":", rent[i])
                    if returnTime > rentalTime:
                        print("Exceeded Months:", rent[2])
                        print("Exceeded Months Penalty:", rent[1])
                    messages.dashes()
        messages.dashes()
        print("Total Price of", len(landList), "land:", rent[0])
        messages.dashes()
        write.storeReturnInvoiceData(name, landList, returnDateList, rentalTime, returnTime)
    except Exception as e:
        messages.plusLines("An error occurred: " + str(e))

def uniqueValue():
    """
    Generates a unique value based on the current time.

    Returns:
        str: A unique string based on current minute, second, and microsecond.
    """
    try:
        uniqueValue = str(datetime.datetime.now().minute) + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond)
        return uniqueValue
    except Exception as e:
        messages.plusLines("An error occurred: " + str(e))
        return ""

def returnLand(name):
    """
    Handles the process of returning rented land, including validation and updating land availability.

    Args:
        name (str): The name of the customer returning the land.
    """
    try:
        land_data = read.readDataFromFile("Rental Data.txt")
        landId = int(input("Enter the land id of the land you've rented: "))

        landReturn = True
        landList = []
        while landReturn:
            if landId < 1 or landId > len(land_data):
                messages.plusLines("Invalid Land ID!! Please enter a valid Land ID.")
                landId = int(input("Enter the land id of the land you've rented: "))
            else:
                if land_data[landId][5] == "Not Available":
                    if landId in land_data:
                        landList.append(landId)
                        rentalTime = int(input("How long did you rent the land? "))
                        returnTime = int(input("After how long did you return the land? "))

                        write.changeLandAvailability(landId)
                    else:
                        messages.plusLines("This land is currently not rented: ")
                else:
                    messages.plusLines("Sorry, the land is not rented. Please enter a valid land id.")
                    landId = int(input("Enter the land id of the land you've rented: "))
                validDecision = False
                while not validDecision:
                    decision = input("Do you want to return more lands that are available? (Y/N): ")
                    if decision.lower() == "n":
                        validDecision = True
                        landReturn = False
                    elif decision.lower() == "y":
                        landId = int(input("Enter the land id of the land you've rented: "))
                        validDecision = True
                    else:
                        messages.plusLines("Invalid entry!! Please enter a valid input.")
                        validDecision = False
        returnInvoice(name, landList, rentalTime, returnTime)
    except Exception as e:
        messages.plusLines("An error occurred: " + str(e))
