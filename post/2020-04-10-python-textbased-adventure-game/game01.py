# Setup
from textwrap import dedent
yes_no = ["yes", "no"]
directions = ["west", "east", "south", "north"]

# Start of game
response = ""
while response not in yes_no:
    response = input("\nYou are in front of an old white house. Would you like to step in?(yes/no)\n")
    if response == "yes":
        print("\nThere's a wooden door in front of you. It's locked from inside.")
    elif response == "no":
        print("\nGoodbye.")
        quit()
    else:
        print("\nI didn't understand that.\n")

#Old House
response = ""
while response not in directions:
    response = input("What direction do you want to move? (west/east/north/south)\n")
    if response == "west":
        print("\nYou're in the west of house. You see a window but it's locked.")
        response = ""
    elif response == "east":
        print("\nYou're in the east of house. There's an open, small window.")
    elif response == "south":
        print("\nYou're already in the south of house. You can see a locked door in front of you.")
        response = ""
    elif response == "north":
        print("\nYou're now in the north of house. There's nothing in here.")
        response = ""
    elif response == "exit":
        print("\nYou leave the house. Goodbye,")
        quit()
    else:
        print("\nI didn't understand that.\n")

#Kitchen
response = ""
while response not in yes_no:
    response = input("Do you want to open the window? (yes/no) \n")
    if response == "yes":
        desc = dedent("""
        You find yourself standing in a kitchen. There's some food on a table.
        On the corner, you can see a brass lantern and a knife on the counter.
        A hallway is in the west of the kitchen.
        """)
        print(desc)
    elif response == "no":
        print("\nGoodbye.")
        quit()
