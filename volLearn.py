import json
import os


inputFile = "C:/Users/mgrub/Desktop/senior year/firstSemesterSenior/Memory Forensics/MemoryForensicsFinalProject/volLearn-input1.json"

#===============================================================================================================
#   >>> Create Main Menu
def createMenu():
    print("\t\t\t\t\tVolLearn - 2019")
    print("\t\t\tLearn Volatility the Easy Way")
    print("=====================================================")
    print("\t\t\t\t\t ---> MENU <---")
    print("\t\t\tLEARN")
    print("1. What is Memory Forensics?")
    print("2. What is Volatility?")
    print("3. Commonly used Volatility plugins")
    print("4. ")
    print("5. Take a Test")
    print("------------------------------------")
    print("\t\t\tPRACTICE")
    print("6. How to write a Volatility command")
    print("\nEnter 'quit' to exit program\n")
#===============================================================================================================


def decision1():
    print("\nWhat is Memory Forensics\n----------------------------------")
    print("----> MUST PUT IN BEFORE SUBMISSION")
    input("Press any key to continue...\n\n")

def decision5():
    print("\nTake a Test\n----------------------------------")
    print("----> MUST PUT IN BEFORE SUBMISSION")
    input("Press any key to continue...\n\n")

def decision6():
    print("\nHow to write a Volatility command\n----------------------------------")
    print("To properly write a Volatility plugin, the following format must be followed:\tvolatility --profile='selected profile' -f 'path/to/memorydump' plugin")
    print("If the command is not typed in this format, an error could occur where Volatilty is not able to process the command. "
          "This error is often hard to identify. To eliminate this risk, model all future Volatility commands after this template")
    input("\nPress any key to continue...\n\n")


#===============================================================================================================
#===============================================================================================================
#       >>> Main Loop
if __name__ == "__main__":
    while True:
        isString = False
        isInt = False
        createMenu()

        decision = input("Select an option: ")             # get input from user .... will be in 'str' format


        # ===================================================================================
        #       >>> Handle input from user
        if decision == "quit" or decision == "quit ":                             # if input is string 'quit'
            print("Thank you for using volLearn!!")
            quit()
        if decision != "quit":                             # if input isn't 'quit', convert to int
            try:
                decision = int(decision)
            except ValueError:                             # if input can't be converted to int, throw an exception and ask the user again
                print("--> Error.... Please enter the number for an option on the menu\n")
                continue
        # ===================================================================================

        print("")


        # ===================================================================================
        #       >>> Call the respective function for each decision
        if decision == 1:
            decision1()
        if decision == 5:
            decision5()
        if decision == 6:
            decision6()







    #    if decision <= 0:
       #     print("\n\n----> ERROR ..... That option is not available from the menu")



