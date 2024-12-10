# Imports proper libraries for this program to function.
import time
import os
import sys


"""
This program is intended to mostly reach python platforms without unified
  shell standards to assist with system commands and administration.
"""


"""
Variable declarations. "print" is not an actual package manager.
 It's just there for intended program design.
"""

hostList = ("print", "winget", "apt", "pacman", "portage", "xbps", "yay", "dnf")
credit = ("Original defunct c++ write(by me) [c++ is hard ); ]",)


"""
Prompts for terminal commands to run, while keeping count
  of the amount of commands entered.
"""
def getCommands():
    control = 0
    while True:
        com = input("Please enter a command (or [q] to quit): \n")

        if com != "q":
            commands.append(com)
            control += 1
            print("You have " + str(control) + " command/s")
            print("")
            continue

        print("")
        return control
        break


# For debug purposes
def clearCommands():
    commands = []


"""
Assists users with basic package management for the target system if supported.
  This was not going to be added, but the program flopped sysadmin wise,
  so it's staying in.
"""
def assistedCommands():
    print("Warning: Expect problems. This was not the program's initial intended purpose, but was made as an assistance tool.")
    print("")

    while True:
        host = input("What is your package manager? (type \"print\" to see available package managers): ")

        if host.lower() not in hostList:
            print("Error: Package manager not found. If your package manager is not in the host variable, assisted commands will be unavailable.")

        elif host.lower() == "winget":
            presetCommands = {
                "update":"winget update ",
                "install":"winget install ",
                "remove":"winget remove "
            }
            break

        elif host.lower() == "apt":
            presetCommands = {
                "update":"sudo apt update && sudo apt upgrade",
                "install":"sudo apt install ",
                "search":"apt search ",
                "remove":"sudo apt remove "
            }
            break

        elif host.lower() == "pacman":
            presetCommands = {
                "update":"sudo pacman -Syu",
                "install":"sudo pacman -S ",
                "search":"pacman -Ss ",
                "remove":"sudo pacman -R "
            }
            break
  
        elif host.lower() == "portage":
            presetCommands = {
                "update":"emerge --ask --verbose --update --newuse --deep @world",
                "install":"emerge --ask ",
                "search":"emerge --search ",
                "remove":"emerge --ask --verbose --depclean "
            }
            break

        elif host.lower() == "xbps":
            presetCommands = {
                "update":"sudo xbps-install -u xbps && sudo xbps-install -Syu",
                "install":"sudo xbps-install -S ",
                "search":"xbps-query ",
                "remove":"sudo xbps-remove "
            }
            break

        elif host.lower() == "yay":
            presetCommands = {
                "update":"yay",
                "install":"yay -S ",
                "search":"yay -Ss ",
                "remove":"yay -R "
            }
            break

        elif host.lower() == "dnf":
            presetCommands = {
                "update":"sudo dnf upgrade",
                "install":"sudo dnf install ",
                "search":"dnf search ",
                "remove":"sudo dnf remove "
            }
            break

        elif host.lower() == "print":
            print(hostList[1:])
            continue

        else:
            print("An error occurred. Please try again.")
            continue

    print("Here are your commands: ")

    print(presetCommands.keys())
    print("")
    
    while True:
        term = input("What operation would you like to perform? (any of the previously mentioned, or [q]uit): ")

        if term.lower() == "q":
            print("Canceling...")
            break

        elif term.lower() == "update":
            if host.lower() == "winget":
                packages = input("Enter the package/s in question: ")
                os.system(presetCommands[term] + packages)
            
            else:
                os.system(presetCommands[term])

        elif term.lower() not in presetCommands:
            print("Invalid operation. Please check the output of \"Here are your commands:\".")
            continue
        
        else:
            packages = input("Enter the package/s in question: ")
            os.system(presetCommands[term] + packages)

    
# Runs the commands in the commands variable with appropriate delay intervals.
def runCommands(initDelay, intervalDelay):
    time.sleep(initDelay)

    for i in range(len(commands)):
        os.system(commands[i])
        time.sleep(intervalDelay)
        print("")


# Introduction block
print("This program can help you execute terminal commands in sequence.")
time.sleep(1)
print("")


"""
Prompts the user to confirm that they wish to run the program. Exits execution
  if the user enters "n".
"""
begin = input("Would you like to run the program? ([y]es or [n]o): ")


# Initializes the main program loop.
while True:

    # The most significant variable of this program.
    commands = []

    # Prompts for user preffered operation.
    if begin.lower() == "y":
        helpme = input("Would you like to get assisted commands? ([y]es or [n]o): ")
        print("")

        # Runs assisted commands.
        if helpme.lower() == "y":
            assistedCommands()
        
        elif helpme.lower() == "cmd":
            os.system("python -i taskVF.py")

        # Runs manual commands.
        else:
            print("Manual commands activated.")
            control = getCommands()
            print("Final command count: " + str(control) + " command/s")
            time.sleep(1)
            cont = input("Would you like to continue? ([y]es or [n]o): ")

            if cont.lower() == "y":
                print("")

                try:
                    initDelay = int(input("How long do you want the initialization to wait(in seconds)? "))
                except ValueError:
                    valueControl = 1
                    while valueControl != 0:
                        try:
                            initDelay = int(input("Bad value. Try again: "))
                            valueControl = 0
                        except ValueError:
                            continue

                try:
                    intervalDelay = int(input("How long do you want each command to wait after the previous? "))
                except ValueError:
                    valueControl = 1

                    while valueControl != 0:
                        try:
                            intervalDelay = int(input("Bad value. Try again: "))
                            valueControl = 0
                        except ValueError:
                            continue
                print("")
                runCommands(initDelay, intervalDelay)

            elif cont.lower() != "y" and cont.lower() != "n":
                print("Invalid answer detected. Assuming answer was [n]o...")
        
            else:
                print("Canceled.")
                break
        
    else:
        print("Stopping program execution...")
        sys.exit()
        
    # Cleanup code block.
    clearScreen = input("Would you like to clear the screen? ([y]es or [n]o): ")
    
    if clearScreen.lower() == "y":
        os.system("clear")
    
    cred = input("Would you like to see the credits? ([y]es or [n]o): ")
    
    if cred.lower() == "y":
        for i in range(len(credit)):
            print(credit[i])
            time.sleep(0.5)
    print("")

    rerun = input("The program has finished. Would you like to re-run the program? ([y]es or [n]o): ")
    
    if rerun.lower() == "y":
        continue
    
    else:
        if clearScreen.lower() == "y":
            os.system("clear")
        sys.exit()

# End of program.
