# Imports proper libraries for this program to function.
import time
import os
import sys


"""
This program is optimized for system admins (mostly linux system admins),
  who need a way to execute commands in a sequence, while having
  opportunities to review the output of commands before the next one
  executes.
"""


# The most significant variable of this program.
commands = []


# Other variables
hostList = ("winget", "apt", "pacman", "portage", "xbps")
credit = ("Original defunct c++ write (c++ is hard ];)",)


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


def assistedCommands():
    print("Warning: Expect problems. This program is not made for users that need assistance with these tasks.")
    print("")
    
    while True:
        host = input("What is your package manager? (winget, apt, pacman, portage, or xbps): ")
        
        if host.lower() not in hostList:
            print("Invalid package manager. If your package manager is not in the host variable, you will have to use this tool manually.")
        
        elif host.lower() == "winget":
            presetCommands = {
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
                "install":"sudo pacman -S  ",
                "search":"pacman -Ss ",
                "remove":"sudo pacman -R  "
            }
            break
            
        elif host.lower() == "portage":
            presetCommands = {
                "update":"emerge --ask --verbose --update --newuse --deep @world",
                "install":"emerge --ask  ",
                "search":"emerge --search ",
                "remove":"emerge --ask --verbose --depclean "
            }
            break
        
        elif host.lower() == "xbps":
            presetCommands = {
                "update":"sudo xbps-install -u xbps && sudo xbps-install -Syu",
                "install":"sudo xbps-install -S  ",
                "search":"xbps-query  ",
                "remove":"sudo xbps-remove "
            }
            break
        
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
        helpme = input("Would you like to get assisted commands? This is NOT recommended. ([y]es or [n]o): ")
        print("")
        
        if helpme.lower() == "y":
            assistedCommands()
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