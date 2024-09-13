import messages

def readDataFromFile(fileAdd):
    """
    Reads land data from a specified file and returns it as a dictionary.

    Args:
        fileAdd (str): The path to the file from which to read the land data.

    Returns:
        dict: A dictionary where the keys are land IDs (integers) and the values are lists containing land details.
    """
    land_data = {}
    try:
        i = 1   
        file = open(fileAdd, "r+")
        for line in file:
            line = line.replace("\n", "")
            line = line.split(", ")
            line[0] = int(line[0])
            line[3] = int(line[3])
            line[4] = int(line[4])
            land_data[i] = line
            i += 1
        file.close()
        return land_data
    except FileNotFoundError:
        print("Error: " + fileAdd + " not found!!")
    except:
        print("Error !!! Another Expception encountered")

def displayTable(land_data):
    """
    Displays a formatted table of land data.

    Args:
        land_data (dict): A dictionary where the keys are land IDs and the values are lists containing land details.
    """
    messages.tableLines()
    print("Land ID\t\tKitta No.\t\tCity/Disrict Name\t\tDirection\t\tAnna\t\tPrice(NRs.)\tAvailability Status")
    messages.tableLines()
    for key, value in land_data.items():
        print(key, "\t\t", value[0], "\t\t\t", value[1], "\t\t\t", value[2], "\t\t\t", value[3], "\t\t", value[4], "\t\t", value[5])
    messages.tableLines()
    print("\n")
