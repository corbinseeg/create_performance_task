# Imports proper libraries for this program to function.
import time
import os
import sys


"""
This program is made for system admins (mostly linux system admins),
  who need a way to execute commands in a sequence, while having
  opportunities to review the output of commands before the next one
  executes.
"""

# The most significant variable of this program.
commands = []


"""
Prompts for terminal commands to run, while keeping count
  of the amount of commands entered.
"""
def getCommands():
    control = 0
    while True:
        com = input("Please enter a command (or [q] to quit): ")
        if com != "q":
            commands.append(com)
            control += 1
            print("You have " + str(control) + " command/s")
            print("")
            continue
        print("")
        return control
        break


# Runs the commands in the commands variable with appropriate delay intervals.
def runCommands(initDelay, intervalDelay):
    time.sleep(initDelay)
    for i in range(len(commands)):
        os.system(commands[i])
        time.sleep(intervalDelay)
        print("")


print("This program can help you excecute terminal commands in sequence.")
time.sleep(2)
print("")


"""
Prompts the user to confirm that they wish to run the program. Exits execution
  if the user enters "n".
"""
begin = input("Would you like to run the program? ([y]es or [n]o): ")

# Initializes the main program loop.
while True:
    if begin.lower() == "y":
        control = getCommands()
        print("Final command count: " + str(control) + " command/s")
        time.sleep(1)
        cont = input("Would you like to continue? ([y]es or [n]o): ")
        if cont.lower() == "y":
            print("")
            initDelay = int(input("How long do you want the initialization to wait(in seconds)? "))
            intervalDelay = int(input("How long do you want each command to wait after the previous? "))
            print("")
            runCommands(initDelay, intervalDelay)
        else:
            print("Canceled.")
            break
    else:
        print("Stopping program execution...")
        sys.exit()
    clearScreen = input("Would you like to clear the screen? ([y]es or [n]o): ")
    if clearScreen.lower() == "y":
        os.system("clear")
    rerun = input("The program has finished. Would you like to re-run the program? ([y]es or [n]o): ")
    if rerun.lower() == "y":
        continue
    else:
        if clearScreen.lower() == "y":
            os.system("clear")
        sys.exit()
