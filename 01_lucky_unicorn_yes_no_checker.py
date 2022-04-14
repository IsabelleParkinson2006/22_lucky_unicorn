show_instruction = input("Have you played this game before?").lower()
if show_instruction == "no" or show_instruction == "n":
    print("Display instructions.")
elif show_instruction == "yes" or show_instruction == "y":
    print("Program continues.")
elif show_instruction != "yes" or show_instruction == "y" or show_instruction == "no" or show_instruction == "n":
    print("Please choose yes/no")
