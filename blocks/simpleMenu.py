#!/usr/bin/env python
import os


def Menu():
    os.system('clear')
    print """
    ================================
    Simple Menu
    ================================
    1 - do A action
    2 - do B action
    3 - do C action
    4 - do D action
    5 - do E action
    6 - Exit
    ================================
    """
    choice = raw_input("Enter a choice and press enter:  ")
    return choice

#TAKE CHOICE AND LAUNCH MODULE

choice = ""

while choice != "6":
    choice = Menu()
    if choice == "1":
        os.system('clear')
        print 'A'
        raw_input("Press enter to continue:  ")
    elif choice == "2":
        os.system('clear')
        print 'B'
        raw_input("Press enter to continue:  ")
    elif choice == "3":
        os.system('clear')
        print 'C'
        raw_input("Press enter to continue:  ")
    elif choice == "4":
        os.system('clear')
        print 'D'
        raw_input("Press enter to continue:  ")
    elif choice == "5":
        os.system('clear')
        print 'E'
        raw_input("Press enter to continue:  ")
