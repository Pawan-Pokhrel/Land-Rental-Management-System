import messages
import read
import operations
import datetime

def changeLandAvailability(landId):
    """
    Toggles the availability status of the land identified by landId.
    Updates the land's status between "Available" and "Not Available" in the data file.

    Args:
        landId (int): The ID of the land whose availability status is to be changed.
    """
    try:
        fileAdd = "Rental Data.txt"
        land_data = read.readDataFromFile(fileAdd)
        updated_data = {}
        for key, value in land_data.items():
            if(key == landId):
                if(value[5] == "Available"):
                    value[5] = "Not Available"
                else:
                    value[5] = "Available"
            updatedLine = [value[0], value[1], value[2], value[3], value[4], value[5]]
            updated_data[key] = updatedLine
        file = open(fileAdd, "w")
        for key, value in updated_data.items():
            strValue = []
            for each in value:
                each = str(each)
                strValue.append(each)
            file.write(', '.join(strValue) + "\n")
        file.close()
    except Exception as e:
        print(f"An error occured while updating the land availability status!! {e}")

def storeRentInvoiceData(name, landList, rentalTimeList):
    """
    Creates a text file with a rental invoice for the rented lands.

    Args:
        name (str): The name of the customer.
        landList (list): List of land IDs rented.
        rentalTimeList (list): List of rental times for each land ID.
    """
    rentalFullDate = datetime.datetime.now()
    rentalTime = str(rentalFullDate.year) + "-" + str(rentalFullDate.month) + "-" + str(rentalFullDate.day) + "\t" + str(rentalFullDate.hour) + ":" + str(rentalFullDate.minute) + ":" +str(rentalFullDate.second)
    uniqueValue = operations.uniqueValue()
    fileName = ("Rent_" + name + "_" + uniqueValue + ".txt")
    file = open(fileName, "w")
    rent = operations.totalRent(landList, rentalTimeList)
    land_data = read.readDataFromFile("Rental Data.txt")
    j = 1
    for key, value in land_data.items():
        for i in range(len(landList)):
            if(key == landList[i]):
                file.write(str(j) + " )\n")
                j += 1
                file.write("Name of the rental customer: " +  name + "\n")
                file.write("Land ID: " + str(key) + " \n")
                file.write("Kitta No.:" +str(value[0]) + " \n")
                file.write("City/District Name: " + value[1] + " \n")
                file.write("Direction the land is facing: " + value[2] + " \n")
                file.write("Anna: " + str(value[3]) + " \n")
                file.write("Price per Anna per month: " + str(value[4]) + " \n")
                file.write("Land Rented for: " + str(rentalTimeList[i]) + " months\n")
                file.write("Total price of Land ID No. " + str(key) + " : " + str(rent[0][i]) + " \n")
                file.write("Land Rented on " + str(rentalTime) + " \n")
                file.write("---------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Total Price of " + str(len(landList)) + " land: " + str(rent[1]))   

def storeReturnInvoiceData(name, landList, returnDateList, rentalTime, returnTime):
    """
    Creates a text file with a return invoice for the returned lands.

    Args:
        name (str): The name of the customer.
        landList (list): List of land IDs being returned.
        returnDateList (list): List of return dates for each land ID.
        rentalTime (int): The initial rental time.
        returnTime (int): The time when the land is returned.
    """
    returnFullDate = datetime.datetime.now()
    returnnTime = str(returnFullDate.year) + "-" + str(returnFullDate.month) + "-" + str(returnFullDate.day) + "\t" + str(returnFullDate.hour) + ":" + str(returnFullDate.minute) + ":" +str(returnFullDate.second)
    uniqueValue = operations.uniqueValue()
    fileName = ("Return_" + name + "_" + uniqueValue + ".txt")
    file = open(fileName, "w")
    rent = operations.totalReturningRent(landList, rentalTime, returnTime)
    land_data = read.readDataFromFile("Rental Data.txt")
    j = 1
    for key, value in land_data.items():
        for i in range(len(landList)):
            if(key == landList[i]):
                file.write(str(j) + " )\n")
                j += 1
                file.write("-----------------------------------------------------------------\n")
                file.write("Name of the rental customer: " +  name + "\n")
                file.write("Land ID: " + str(key) + " \n")
                file.write("Kitta No.:" +str(value[0]) + " \n")
                file.write("City/District Name: " + value[1] + " \n")
                file.write("Direction the land is facing: " + value[2] + " \n")
                file.write("Anna: " + str(value[3]) + " \n")
                file.write("Price per Anna per month: " + str(value[4]) + " \n")
                file.write("Land Rented for: " + str(rentalTime) + " months\n")
                file.write("Fine Amount: " + str(rent[1])+"\n")
                file.write("Total price of Land ID No. " + str(key) + " : " + str(rent[0]) + " \n")
                file.write("Land Returned on " + str(returnnTime) + " \n")
                if(returnTime > rentalTime):
                    file.write("Exceeded Months:" + str(rent[2]))
    file.write("\n\n")
    file.write("Total Price of " + str(len(landList)) + " land: " + str(rent[0]))   
