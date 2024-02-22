# The Time Library allows for the sleep function
import time

def printArray(delay, array):
    for line in array:
        print(line)
        time.sleep(delay)

# This defines a function that starts the walk cycle
def walk(max):
    # Set the steps to start as 0
    steps = 0
    totalSteps = 0
    while True:
        # This will ask the user how many steps they want to walk and add it to the total steps
        steps = int(input("How many steps will you walk? "))
        totalSteps += steps
        # This will loop through the steps and print a message
        for i in range(steps):
            # An f string is used so varaible can be passed within it without concatanating
            print(f"Taking Step ({i+1}/{steps})...")
            # Sleep to wait for one second
            time.sleep(1)
        # If the steps is more than the max, return false
        if totalSteps > max:
            return False
        else:
            # Ask the user if they want to continue, if they don't, return the steps
            print("Nothing bad happend!")
            again = input("Would you like to keep walking? (y/n)")
            if again == "n":
                return totalSteps
            time.sleep(1)

def beach():
    print("You begin to walk to the beach...")
    time.sleep(1)
    # Set the max steps variable
    max = 30
    steps = walk(max)
    # If they walked the same as the max, print a message
    if steps == max: 
        print("Amazing! You walked the exact amount of steps you needed to find a beach! You get a gold medal!")
        print("Congrats that is all for now")
    # If there is a steps of any value, print a message
    elif steps: 
        print(f"You have walked {steps} steps and found a beach!")
        print("Congrats that is all for now")
    # If steps is false, print a message
    else:
        print("You have walked too far and got lost in the sea...")\
    # Ask the user if they want to play again
    again = input("Would you like to play again? (y/n)")
    # If they do not, set the loop to false and print goodbye
    if(again == "n"):
        print("Goodbye!")
        return False
    else: return True


def forest():
    print("Sorry, but the forest is not available at this time.")
    again = input("Would you like to play again? (y/n)")
    if(again == "n"):
        print("Goodbye!")
        return False
    else: return True

def playGame():
    # Set the active session to true
    active = True
    # Print the introduction
    print("Perfect! We will now begin...")
    while active:
        time.sleep(1)
        print('You wake up and find yourself stranded on a remote and mysterious deserted island. The island is lush with tropical vegetation, surrounded by clear blue waters...')
        time.sleep(1)
        # Ask the user where they want to go
        location = input("Where would you like to go? b for beach, f for forest ")
        if location == "b":
           active = beach()
        # If user goes to the forest print the message
        elif location == "f":
            active = forest()
        # If the user does not go to the beach or the forest, print multiple messages
        else:
            messages = ["You stay where you are and observe some more...",
                        "You continue to wait...",
                        "You wait longer and longer...",
                        "You begin to get tired and fall asleep..."]
            printArray(1, messages)
            # In this case the loop would continue to make it so the player feels as if they just woke up again


#  Ask the user if they want to play the game
play = input("Hello, and welcome to the deserted island, would you like to play? (y/n)")
if play == "y":
    playGame()
# If the user dose not want to play, print the goodbye message 
else: 
    print("I hope to see you soon, Goodbye")
