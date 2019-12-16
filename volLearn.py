import json
import os
import random


inputFile = "C:/Users/mgrub/Desktop/senior year/firstSemesterSenior/Memory Forensics/MemoryForensicsFinalProject/volLearn-input1.json"

#===============================================================================================================
#   >>> Create Main Menu
def createMenu():
    print("\t\tVolLearn - 2019")
    print("\tLearn Volatility the Easy Way")
    print("=====================================================")
    print("\t\t ---> MENU <---")
    print("\tLEARN")
    print("1. What is Memory Forensics?")
    print("2. What is Volatility?")
    print("3. Commonly used Volatility plugins")
    print("4. ")
    print("5. Take a Test")
    print("------------------------------------")
    print("\tPRACTICE")
    print("6. How to write a Volatility command")
    print("7. Executing your first Volatility command")
    print("\nEnter 'quit' to exit program\n")
#===============================================================================================================


def decision1():
    print("\nWhat is Memory Forensics\n----------------------------------")
    print("----> MUST PUT IN BEFORE SUBMISSION")
    input("Press any key to continue...\n\n")

def decision5():
    print("\nTake a Test")
    numQuestions = input("How many questions would you like to have? (1 to 45): ")
    numQuestions = int(numQuestions)
    print(type(numQuestions))
    print("----------------------------------")

    questions = {
        "\n1. Out of these commands which is a volatiltiy plug-in?\n\ta) cd\n\tb) strings\n\tc) pslists\n\td) ipconfing" : "c",
        "\n2. What does pslsits do in volatiltiy?\n\ta) list all the processes of the system\n\tb) shows the name of the system\n\tc) prints a list of handles" : "a",
        "\n3. What is a PID?\n\ta) A PID helps identifies ip addresses.\n\tb) A PID is the ID number of a process.\n\tc) PID stands for Program In Domain.\n\td) PID's allows to search specific hives." : "b",
        "\n4. On a Pslist what helps you find previous processes that loads a current one?\n\ta) threads\n\tb) handles\n\tc) PID\n\td) PPID" : "d",
        "\n5. What does it mean if a process's handle and thread is 0?\n\ta) the process exists in another system?\n\tb) the process is not active, and may have been terminated\n\tc) that the process has been moved to another hive" : "b"
    }

    questionsRight = 0
    questionsWrong = 0

    questionsTuple = list(questions.items())
    random.shuffle(questionsTuple)
    loopCounter = 0
    for k, v in questionsTuple:
        print(k)
        answer = input("Enter the answer: ")
        if answer != v:
            questionsWrong += 1
        if answer == v:
            questionsRight += 1
        #del k, v
        #print(questionsTuple)
        loopCounter += 1
        if loopCounter == numQuestions:
            break

    totalScore = (questionsRight/numQuestions * 100)
    print("\nRESULTS\n------------------------------------")
    print("Number of questions right: ", questionsRight)
    print("Number of questions wrong: ", questionsWrong)
    print("Total Score: %.2f%%" % totalScore)
    input("\nPress any key to continue...\n\n")



def decision6():
    print("\nHow to write a Volatility command\n----------------------------------")
    print("To properly write a Volatility plugin, the following format must be followed:\tvolatility --profile='selected profile' -f 'path/to/memorydump' plugin")
    print("If the command is not typed in this format, an error could occur where Volatilty is not able to process the command. "
          "This error is often hard to identify. To eliminate this risk, model all future Volatility commands after this template")
    input("\nPress any key to continue...\n\n")

def decision7():
    print("\nExecuting your first Volatility Command\n----------------------------------")
    print("To begin a forensic investigation on a memory dump, the first plugin typically used is 'imageinfo'.")


    input("\nPress any key to continue...\n\n")



#===============================================================================================================
#===============================================================================================================
#       >>> Main Loop
if __name__ == "__main__":
    #with open(inputFile) as json_file:
    #    data = json.load(json_file)
    #print(data)
    #for p in data['pluginList']:
    #    print("Plugin: " + p['plugin'])
    #    print("Output: " + p['output'])

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
        if decision == 7:
            decision7()








        if decision <= 0 or decision > 10:
            print("\n\n----> ERROR ..... That option is not available from the menu. Please pick one that is available.\n")



