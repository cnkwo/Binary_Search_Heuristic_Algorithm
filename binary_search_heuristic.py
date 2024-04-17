# Binary Search Heuristic Algorithm

# Import neccessary modules
import random       # Module for generating random numbers
import time         # Moule for time-related functions
import threading    # Module for creating and managing threads

def selectRandomNumber():
    """
    This function selects a random number after a delay of 3 seconds.

    Returns:
        int: The randomly selected number.
    """
    # 3-second delay
    time.sleep(3)

    # Select random number from list of numbers
    return random.randint(1, 100)

# Genereate list of numbers from 1 to 100
listOfNum = [i for i in range(1,101)]

# Print the generated list of numbers
print("Here is your list of numbers from 1 to 100:\n\n{}\n".format(listOfNum))

# 1-second delay
time.sleep(1)

# Print message indicating that a random number is being selected from the list
print("Now selecting a random number from the list\n")

# 1-second delay
time.sleep(1)

# Print message without a newline character, allowing subsequent output to be on the same line
print("The Random Number that has been selected is", end="")

# Initialize randomNum as None
randomNum = None

# Define a function to continuously print dots while waiting for randomNum to be selected
def printDots():
    """
    Prints dots until `randomNum` is not None.

    This function prints dots ('.') until the global variable `randomNum` is not None,
    indicating that a random number has been selected.

    Returns:
        None
    """
    while randomNum is None:
        print(".", end="")
        time.sleep(0.5)

# Create a thread for printing dots
dot_thread = threading.Thread(target=printDots)
dot_thread.start()

# Call the function to select the random number
randomNum = selectRandomNumber()

# Wait for the dot thread to complete
dot_thread.join()

# Print the randomly selected number
print("{}\n".format(randomNum))

# Print message indicating the start of the search function
print("Now starting search function:\n")

# Define function to find the randomly selected number within the list
def findRandomNum(randomNum, listOfNum):
    """
    This function finds a randomly selected number within a list using a binary search-like algorithm.

    Parameters:
        randomNum (int): The randomly selected number to find within the list.
        listOfNum (list): The list of numbers to search within.

    Returns:
        str: A message indicating whether the randomly selected number was found within the list or not.
    """
    
    # Initialize message variable
    message = ""

    # Continue loop until the randomly selected number is found
    while True:

        # Pause execution for 1 second
        time.sleep(1)

        # Calculate middle index of the list
        middleIndex = len(listOfNum) // 2

        # Check if the length of the list is odd number
        if len(listOfNum) % 2 == 1:
            # If odd, middle number is the element at middle index
            middleNum = listOfNum[middleIndex]

        # Check if the length of the list is even and not 2
        elif len(listOfNum) % 2 == 0 and len(listOfNum) != 2 :
            # If even, adjust middle index and get the middle number
            middleIndex = len(listOfNum) // 2 -1
            middleNum = listOfNum[middleIndex]

        # If the list length is 2
        else:
            # For list length 2, middle number is the first element (for simplicity)
            middleNum = listOfNum[0]

        # Compare the randomly selected number with the middle number
        if randomNum == middleNum:
            # If they match, set success message and return
            message = "Wow the algorithm has found the correct number, {} !".format(randomNum)
            return message
        elif randomNum < middleNum:
            # If randomly selected number is less than middle number, narrow search to first half of list
            listOfNum = listOfNum[:middleIndex + 1]
            message = "Still not found. The correct number is less than the current selection {}".format(middleNum)
        else:
            # If randomly selected number is greater than middle number, narrow search to second half of list
            listOfNum = listOfNum[middleIndex:]
            message = "Still not found. The correct number is greater than the current selection {}".format(middleNum)

        # Print progress message
        print(message)

# Call function to find the randomly selected number and store result in variable
searchResult = findRandomNum(randomNum, listOfNum)

# Print final result
print(searchResult)

        

