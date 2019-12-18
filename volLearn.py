#!usr/bin/env python3

import json
import os
import random
from tkinter import filedialog
from tkinter import *



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
    print("4. Output of plugins")
    print("5. Take a Test")
    print("------------------------------------")
    print("\tPRACTICE")
    print("6. How to write a Volatility command")
    print("7. Perform mock investigation")
    print("------------------------------------")
    print("\tCONTRIBUTE TO THE COMMUNITY")
    print("8. Submit a suggestion on how we should improve this.")
    print("9. Sources")
    print("\nEnter 'quit' to exit program\n")


#===============================================================================================================


def decision1():
    print("\nWhat is Memory Forensics\n----------------------------------")
    print("----> MUST PUT IN BEFORE SUBMISSION")

# What is Volatility?
def decision2():
    print("\nWhat is Volatility\n----------------------------------")
    print("Volatility is one of the best open source software programs for analyzing RAM in 32 bit/64 bit systems. It supports analysis for Linux, Windows, Mac, and Android systems. It is based on Python and can be run on Windows, Linux, and Mac systems. It can analyze raw dumps, crash dumps, VMware dumps, virtual box dumps, and many others. Volatility, memory forensics framework, is capable to perform monitoring runtime processes and state of any system using the data found in RAM. Therefore, it can perform reconnaissance on process lists, ports, network connections, registry files, DLL’s, crash dumps and cached sectors. This framework also provides a unique platform that enables better efficiency of Forensic research (Law Enforcement, defense forces, commercial investigators, etc. Volatility supports memory dumps from all Windows versions and service packs including XP, 2003 Server, Vista, Server 2008, Server 2008 R2, and Seven. It also supports Linux memory dumps and distributions such as Debian, Ubuntu, Fedora, CentOS, and Mandrake. The memory forensics framework supports Mac OSX memory dumps, Mountain Lion, Android phones with ARM processors.")
    input("Press any key to continue...\n\n")


# Commonly used Volatility plugins
def decision3():

    ImageIDDict = {
        "\timageinfo" : "\n---------------------------------------------\nWhen the user is trying to perform an evaluation test when using Volatility, we need to set a profile so that Volatility can select which OS the memory dump is using. When you have the memory dump and you do not know which profile to select, you can use imageinfo. Imageinfo gives you different profiles of the memory dump, different layers, number of processors, image time and date, and other factors for the memory dump.\n----------------------------------------------\nUse of plugin in command: 'volatility imageinfo -f /path/to/dumpfile'",
        "\tkdbgscan" : "\n---------------------------------------------\nThis plugin is designed to positively identify the correct profile and the correct KDBG address. This plugin scans for the KDBGHeader signatures linked to Volatility profiles and applies sanity checks to reduce false positives.\n----------------------------------------------\nUse of plugin in command: 'volatility kdbgscan -f /path/to/dumpfile --profile=WinXPSP2x86'"
    }

    ProcessesDllsDict ={
        "\tpslist" : "\n---------------------------------------------\nIf you need to show a high view of all the running processes from a memory dump in Volatility, you use pslist. Pslist will show the name of the process, the process ID number, the parent process ID number, the number of threads and handles, and the offset. Pslist will show you so much but it cannot detect hidden or unlinked processes.\n----------------------------------------------\nUse of plugin in command: 'volatility pslist -f /path/to/dumpfile --profile=WinXPSP2x86",
        "\tpsscan" : "\n---------------------------------------------\nPsscan is used for finding processes that were terminated or inactive and processes that are hidden or unlinked by using rootkit. Since pslist cannot find the hidden/unlinked processes, psscan is capable of this task. Rootkits can still hide by being overwritten by pool tags. Psscan includes offset, name of the exe. file, process ID, parental process ID, time created, and time exited.\n----------------------------------------------\n.Use of plugin in command: 'volatility psscan -f /path/to/dumpfile --profile=WinXPSP2x86'",
        "\tconsoles" : "\n---------------------------------------------\nThis is a plugin that shows what the hacker has typed into the command prompt of the computer and it shows all the information corresponding to those actions. It collects the input and outputs of these actions and also prints the command that was written. With each command that is being printed, it shows the address that matches with it.\n----------------------------------------------\nUse of plugin in command: 'volatility consoles -f /path/to/dumpfile --profile=Win7SP0x86'",
        "\tprivs" : "\n---------------------------------------------\nThis plugin shows you the privileges that are present in the process's token, which have been enabled, and which were enabled by default. If any privileges are enabled by not enabled by default, you know they were explicitly set. If any privileges are enabled but not present, that's a strong indicator of DKOM.\n----------------------------------------------\nUse of plugin in command: 'volatility privs -f /path/to/dumpfile dmp --profile=WinXPSP2x86'",
        "\thandles" : "\n---------------------------------------------\nIf you want to see the open handles in a process, you use this plugin. It will show you the offset, Pid, handle, access, and the type. This plugin is associated with registry keys, events, desktops, files, threads, and mutexes.\n----------------------------------------------\nUse of plugin in command: 'volatility handles -f /path/to/dumpfile --profile=WinXPSP2x86'",
        "\tpstree" : "\n---------------------------------------------\nIn order to view processes in a tree form listing, use this plugin. This tallies up processes using similar techniques as pslist so it will also not show hidden or unlinked processes.\n----------------------------------------------\nUse of plugin in command: 'volatility pstree -f /path/to/dumpfile --profile=WinXPSP2x86'",
        "\tpsxview" : "\n---------------------------------------------\nThis plugin helps you detect hidden processes by comparing what PsActiveProcessHead contains with what is reported by various other sources of process listings.\n----------------------------------------------\nUse of plugin in command: 'volatility psxview -f /path/to/dumpfile --profile=WinXPSP2x86'"
    }

    ProcessMemDict = {
        "\tiehistory" : "\n---------------------------------------------\nThis plugin is used for showing the history and cache files and it finds links and entries.\n----------------------------------------------\nUse of plugin in command: 'volatility iehistory -f /path/to/dumpfile --profile=WinXPSP2x86'",
        "\tprocdump" : "\n---------------------------------------------\nIn order to dump a processes executable file, use this plugin. If you use the “-u” in the command, you can bypass certain checks and restrictions.\n----------------------------------------------\nUse of plugin in command: 'volatility procdump -f /path/to/dumpfile --profile=WinXPSP2x86'",
        "\tmemdump" : "\n---------------------------------------------\nIn order to extract all of the memory into a single file, use this plugin.\n----------------------------------------------\nUse of plugin in command: 'volatility memdump -f /path/to/dumpfile --profile=WinXPSP2x86'"
    }

    KernelDict = {
        "\tmodules" : "\n---------------------------------------------\nIn order to view the list of drivers in the kernel that are loaded onto the system, you have to use this plugin. It shows the base, the size, the file path, and the name of the file.\n----------------------------------------------\nUse of plugin in command: 'volatility modules -f /path/to/dumpfile --profile=WinXPSP2x86'"
    }

    NetworkingDict = {
        "\tconnections" : "\n---------------------------------------------\nIn order to view all of the TCP connections from the memory dump that are active, you have to use the connections plugin. The concepts associated with this plugin are offsets, local address, remote address, and the process ID.\n----------------------------------------------\nUse of plugin in command: 'volatility connections -f /path/to/dumpfile --profile=Win7SP0x86'",
        "\tnetscan" : "\n---------------------------------------------\nIn order to scan for network findings, you have to use netscan. This plugin will find TCP endpoints and listeners and also UDP endpoints and listeners. It shows the offset, local address, foreign address, the state of the offset, and others. Netscan command will use pool tag scanning.\n----------------------------------------------\nUse of plugin in command: 'volatility netscan -f //path/to/dumpfile --profile=Win7SP0x86'"
    }

    RegistryDict = {
        "\thivescan" : "\n---------------------------------------------\nIn order to find the physical address of the registry hives in the memory, you can use hivescan. It is supposed to be used along with another plugin such as hivelist and not used by itself.\n----------------------------------------------\nUse of plugin in command: 'volatility hivescan -f /path/to/dumpfile dmp --profile=WinXPSP2x86'",
        "\thivelist" : "\n---------------------------------------------\nWhen using the hivelist plugin, it allows you to print a list of all the current registry hives that were located in the memory dump. When you run this plugin on Volatility, it gives you all the virtual addresses, physical addresses, and the path from where it is stored in the computer of the memory dump. You can also be specific to a certain hive and run the test for that.\n----------------------------------------------\nUse of plugin in command: 'volatility hivelist -f /path/to/dumpfile --profile=Win7SP0x86'",
        "\thashdump" : "\n---------------------------------------------\nThis plugin is used for obtaining and decrypting the passwords of the user’s computer that is stored in the registry. For a more specific search, you can put the allotted address to directly search in there for possible passwords.\n----------------------------------------------\nUse of plugin in command: 'volatility hashdump -f /path/to/dumpfile --profile=Win7SP0x86'",
        "\tprintkey" : "\n---------------------------------------------\nIn order for you to see the values, data, subkeys, and data types within a specific registry key, you should use printkey. The plugin will search all hives and print the information, if it was found, for that specific key. For example if a key is found in more than one location, the information for that key will be printed for as many times it is found.\n----------------------------------------------\nUse of plugin in command: 'volatility printkey -f /path/to/dumpfile dmp --profile=WinXPSP2x86'"
    }



    print("\nCommonly used Volatility plugins\n----------------------------------")
    print("What plugins would you like to review:\n\t1. Image Identification\n\t2. Processes and DLLs\n\t3. Process Memory\n\t4. Kernel Memory and Objects\n\t5. Networking\n\t6. Registry\n\t7. Crash, Hashdumps and Conversion\n\t8. File System\n\t9. Miscellanous\n")
    decision = input("Enter decision: ")
    print("")
    decision = int(decision)

    if decision > 9 or decision < 0:
        print("Error.... Incorrect input, please enter in an option from the menu above.")
        decision3()
    if decision == 1:
        ImageIDDictTuple = list(ImageIDDict.items())
        for k, v in ImageIDDictTuple:
            print(k, v)
            input("\nHit 'Enter'\n")
    if decision == 2:
        ProcessesDllsDictTuple = list(ProcessesDllsDict.items())
        for k, v in ProcessesDllsDictTuple:
            print(k, v)
            input("\nHit 'Enter'\n")
    if decision == 3:
        ProcessMemDictTuple = list(ProcessMemDict.items())
        for k, v in ProcessMemDictTuple:
            print(k, v)
            input("\nHit 'Enter'\n")
    if decision == 4:
        KernelDictTuple = list(KernelDict.items())
        for k, v in KernelDictTuple:
            print(k, v)
            input("\nHit 'Enter'\n")
    if decision == 5:
        NetworkingDictTuple = list(NetworkingDict.items())
        for k, v in NetworkingDictTuple:
            print(k, v)
            input("\nHit 'Enter'\n")
    if decision == 6:
        RegistryDictTuple = list(RegistryDict.items())
        for k, v in RegistryDictTuple:
            print(k, v)
            input("\nHit 'Enter'\n")
    if decision == 7 or 8 or 9:
        print("Plugins for these sections are not included. Plugins will be updated in future updates of 'volLearn'.\n")



    continueDecision = input("Would you like to continue learning the common plugins?\nType 'yes' or 'no': ")
    if continueDecision == "yes" or "Yes":
        decision3()
    if continueDecision == "no" or "No":
        print("")
    else:
        return


    input("Press any key to return to menu....\n\n")

# Output of plugins
def decision4():

    #root = Tk()
    #root.filename = filedialog.askopenfilename(root, title = "Select the '.json' file that was downloaded with the program.")
    #print(root.filename)

    jsonInputFile = "C:/Users/mgrub/PycharmProjects/volLearn/input.json"

    with open(jsonInputFile) as inputFile:
        data = json.load(inputFile)

        #for p in data['pluginList']:
         #   print("Plugin: " + p['plugin'])
          #  print("Output: " + p['output'])

    print("List of available plugins: ")
    for plugin in data["pluginList"]:
        for name in plugin:
            print("\t", name)
    pluginDecision = input("Please select a plugin whose output you would like to see: ")

    print("\n")
    for plugin in data["pluginList"]:
        if pluginDecision in plugin:
            print("Plugin:", pluginDecision)
            print("Output:\n", plugin[pluginDecision])



    continueDecision = input("\n\nWould you like to see more plugin outputs? 'Yes' or 'No': ")
    if continueDecision == "Yes" or continueDecision == "yes":
        decision4()
    if continueDecision == "No" or continueDecision == "no":
        print("")

# Take a Test
def decision5():
    print("\nTake a Test")
    numQuestions = input("How many questions would you like to have? (1 to 45): ")
    numQuestions = int(numQuestions)
    print("----------------------------------")

    questions = {
        "\n1. Which of the following is a volatiltiy plug-in?\n\ta) cd\n\tb) strings\n\tc) pslists\n\td) ipconfing" : "c",
        "\n2. What does pslsits do in volatiltiy?\n\ta) list all the processes of the system\n\tb) shows the name of the system\n\tc) prints a list of handles" : "a",
        "\n3. What is a PID?\n\ta) A PID helps identifies ip addresses.\n\tb) A PID is the ID number of a process.\n\tc) PID stands for Program In Domain.\n\td) PID's allows to search specific hives." : "b",
        "\n4. On a Pslist, what helps you find previous processes that loads a current one?\n\ta) threads\n\tb) handles\n\tc) PID\n\td) PPID" : "d",
        "\n5. What does it mean if a process's handle and thread is 0?\n\ta) the process exists in another system?\n\tb) the process is not active, and may have been terminated\n\tc) that the process has been moved to another hive" : "b",
        "\n6. What plug-in do you use to find hidden processes?\n\ta) pslist\n\tb) pstree\n\tc) psscan\n\td) handles" : "c",
        "\n7. How does psscan view hidden processes?\n\ta) psscan uses pool tag scanning\n\tb) psscan uses hive tag scanning\n\tc) psscan scans through the hardware" : "a",
        "\n8. What is the downside of psscan?\n\ta) it doesn't have threads in the output\n\tb) it is still a possibility that all the processes is not shown\n\tc) the PPID could lead to a false process" : "b",
        "\n9. What plug-in gives you a summary of the memory that is being analyzed?\n\ta)hivescan\n\tb)hiveslist\n\tc)imageinfo\n\td)iehistory" : "c",
        "\n10. What are one of things you can find in an imageinfo output?\n\ta) profiles\n\tb) ip address\n\tc) computer name\n\td) open sockets" : "a",
        "\n11. With imageinfo you can find the hardware architecture\n\ta) True\n\tb) false" : "True",
        "\n12. What does it mean when there is multiple KCPR addresses regarding an Imageinfo output?\n\ta) that there's multiple service packs\n\tb) that there's malware hidden in memory\n\tc) that there's multiple profiles\n\td) that there's multiple processors" : "d",
        "\n13. What plug-in allows you to see the input and output that was on the command prompt? \n\ta)cmdscan\n\tb)consoles\n\tc)connscan" : "b",
        "\n14. With consoles you are able to see the aliases that correspond with the executed commands.\n\ta) True\n\tb) False" : "True",
        "\n15. Consoles cannot print the name and Pid of attatched processes.\n\ta) True\n\tb) False" : "False",
        "\n16. Connections prints all TCP connections that were active during memory acquistion.\n\ta) True\n\tb) False" : "True",
        "\n17. Connections has the ability to view nonactive connections.\n\ta) True\n\tb) False" : "False",
        "\n18. What plug-in allows you to see active and non-active connections?\n\ta)connections\n\tb)sockscan\n\tc)connscan\n\td)sockets" : "c",
        "\n19. What plug-in finds listeners and endpoints from TCP's and UDP's?\n\ta)sockscan\n\tb)netscan\n\tc)hivescan\n\td)connscan" : "b",
        "\n20. What Windows system is netscan NOT used for?\n\ta) Windows Vista\n\tb) Windows 2008 \n\tc) Windows XP use\n\td) Windows 7" : "c",
        "\n21. To find the physical addresses of registry hives in memory use ____\n\ta) hivescan\n\tb) privs\n\tc) printkey\n\td) imageinfo" : "a",
        "\n22. What makes hivescan hard to use?\n\ta) It only shows the PID's.\n\tb) It only shows the physical address of the hives.\n\tc) it only shows the physical address of the keys." : "b",
        "\n23. What plug-in is an alternative to hivescan?\n\ta) printkey\n\tb) yarascan\n\tc) hiveslist\n\td) pslist" : "c",
        "\n24. What is the job of the hivelist plugin?\n\ta) hivelist gives you the physical address \n\tb) hiveslist gives you the virtual address\n\tc) hiveslist gives you the full paths to certain hives.'\n\td) all the above" : "d",
        "\n25. Does Hiveslist print the keys that are in memory?\n\ta) True\n\tb) False" : "False",
        "\n26. In order to look within the keys, use the ________ plug-in.\n\ta) hivelist\n\tb) privs\n\tc) printkey" : "c",
        "\n27. Does printkey allows you to display the subkeys, values, and data that are in register keys?\n\ta) True \n\tb) False" : "True",
        "\n28. Will printkey help you look for specific keys in your investigation?\n\ta) True\n\tb) False" : "True",
        "\n29. What plug-in do you use to extract and decrypt domain credentials stored in registry?\n\ta) memdump\n\tb) hashdump\n\tc) procdump\n\td) all the above" : "b",
        "\n30. What two virtual address does hashdump need in order to operate?\n\ta) the virtual address of the ntuser.dat hive and SAM hive\n\tb) the virtual address of the SYSTEM hive and the SAM hive\n\tc) the virtual address of the HARDWARE hive and the DEFAULT hive\n\td) both b and c" : "b",
        "\n31. Once the hash is dumped, what can you use the hashes for?\n\ta) find the password\n\tb) find the computer history\n\tc) find the malware" : "a",
        "\n32. Will the hashdump still be significant even if a registry key isn't available in memory?\n\ta) True\n\tb) False" : "False",
        "\n33. What plug-in allows you to see privileges?\n\ta) privs\n\tb) iehistory\n\tc) privilege" : "a",
        "\n34. A privilege is the the permission or authority that process may have to do something in memory\n\ta)True\n\tb)False" : "True",
        "\n35. The _____ flag makes privs only show the privilieges of processes that weren't enabled by default\n\ta) --enable\n\tb) --profile\n\tc) --silent\n\td) --less" : "c",
        "\n36. What is the correct flag if you want see the list of plug-ins available\n\ta)-v\n\tb)-h\n\tc)-s" : "b",
        "\n37. Before using volatility you need the memory dump file that you want to analyze. What flag do you use to get volatility to analyze the file? \n\ta) -f\n\tb) -p\n\tc) -d\n\td) -m" : "a",
        "\n38. Before working with registers you need the flag --profile to implement a profile\n\ta) True\n\tb) False": "True",
        "\n39. What flag do you use before when using the printkey plugin?\n\ta) -h\n\tb) -s\n\tc) -k": "c",
        "\n40. When you use hashdump you need the physical address of the SYSTEM hive and SAM hive. The flag - s is for the SYSTEM and -y for SAM.\n\ta) True\n\tb) False; -y is for SYSTEM and -s is for SAM" : "False",
        "\n41. How do you analyze specefic processes?\n\ta) only use the flag -p\n\tb) use the flag -p then input the PID of the certain processes\n\tc) just put in the PID of the process you want to analyze": "b",
        "\n42. What are registry keys?\n\ta) it is what carries all the data about the system \n\tb) only carries data about hardware\n\tc) only carries data about the processes": "a",
        "\n43. What is volatility?\n\ta) a memory forensics plug-in\n\tb) a private memory forensics framework\n\tc) a open-source memory forensics framework": "c"

    }

    questionsRight = 0
    questionsWrong = 0
    questionsWrongDict = {}


    questionsTuple = list(questions.items())
    random.shuffle(questionsTuple)
    loopCounter = 0
    for k, v in questionsTuple:
        print(k)
        answer = input("Enter the answer: ")
        if answer != v:
            questionsWrong += 1
            questionsWrongDict.update({k : v})

        if answer == v:
            questionsRight += 1

        loopCounter += 1
        if loopCounter == numQuestions:
            break


    if len(questionsWrongDict) is not 0:
        questionsWrongDictTuple = list(questionsWrongDict.items())


    totalScore = (questionsRight/numQuestions * 100)
    print("\nRESULTS\n------------------------------------")
    print("Number of questions right: ", questionsRight)
    print("Number of questions wrong: ", questionsWrong)
    print("Total Score: %.2f%%" % totalScore)

    print("\n\nREVIEW WRONG ANSWERS\n------------------------------------")
    for k, v in questionsWrongDictTuple:
        print(k)
        print("Correct answer: ", v)


    input("\nPress any key to continue...\n\n")



# How to write a Volatility command
def decision6():
    print("\nHow to write a Volatility command\n----------------------------------")
    print("To properly write a Volatility plugin, the following format must be followed:\tvolatility --profile='selected profile' -f 'path/to/memorydump' plugin")
    print("If the command is not typed in this format, an error could occur where Volatilty is not able to process the command. "
          "This error is often hard to identify. To eliminate this risk, model all future Volatility commands after this template")
    input("\nPress any key to continue...\n\n")


# Perform mock investigation
def decision7():
    investigationQuestionsDict = {
        "imageinfo" : "1)	Once you acquired the proper memory dump, what plugin is needed to identify the Operating System and see where the memory dump was taken from? This plugin allows you to basically get a summarization of the file at hand.",
        "psscan" : "2)	Once you pick your profile from the memory dump, what plugin should be executed when trying to find Pid and PPid of the system?",
        "hivelist" : "3)	What plugin is needed in order to show all of the hives to get information regarding the system? This plugin prints a list of registry hives and acknowledges of the virtual addresses.",
        "printkey" : "4)	What plugin is needed in order to print the values of the registry hives that were found? ",
        "consoles" : "5)	What plugin can you use if you want to find out the possible commands the attacker wrote to the cmd.exe? ",
        "netscan" : "6)	How can you find the IP addresses of the hacker’s internet server? ",

    }

    commandFormatDict = {
        "imageinfo" : "volatility imageinfo -f /path/to/dumpfile",
        "psscan" : "volatility psscan -f /path/to/dumpfile --profile=WinXPSP2x86"
    }

    investigationQuestionsDictTuple = list(investigationQuestionsDict.items())
    commandFormatDictTuple = list(commandFormatDict.items())

    print("\nPerform mock investigation\n----------------------------------\n\t\tScenarios")
    for a, b in investigationQuestionsDictTuple:
        print(b)
        answer = input("Your answer: ")
        if answer == a:
            print("Correct, '%s' is the plugin used in this scenario." % a)
        if answer != a:
            print("Incorrect plugin.... The correct plugin for this scenario is: '%s'" % a)

        commandAnswer = input("How would you write this command in volatility?")
        for c, d in commandFormatDictTuple:
            if c == a:
                if commandAnswer == d:
                    print("Correct, that is how you write the volatility plugin.")

                if commandAnswer != d:
                    print("Incorrect.... That is not how you write the plugin.")
                    print("Correct way to write '%s' in volatility: '%s'" % (a, d))
        print("\n")


    input("\nPress any key to continue...\n\n")


def decision8():
    print("Would you like to send an email to one of the creators or would you like to visit out GitHub.com repository?")
    print("Enter 1 for email\nEnter 2 for GitHub repository")
    input(">>> ")

# Sources
def decision9():
    print("Sources\n-------------------------")
    print("The output of the plugins were taken from two GitHub reference pages. These links were used as reference for the plugins.\nURL: https://github.com/volatilityfoundation/volatility/wiki/Command-Reference\nURL: https://github.com/volatilityfoundation/volatility/wiki/Command-Reference-Mal")

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

        print(" ")

        # ===================================================================================
        #       >>> Call the respective function for each decision
        if decision == 1:   # What is Memory Forensics?
            decision1()
        if decision == 2:   # What is Volatility?
            decision2()
        if decision == 3:   # Commonly used Volatility plugins
            decision3()
        if decision == 4:   # Output of plugins
            decision4()
        if decision == 5:   # Take a Test
            decision5()
        if decision == 6:   # How to write a Volatility command
            decision6()
        if decision == 7:   # Perform mock investigation
            decision7()
        if decision == 8:
            decision8()
        if decision == 9:   # Sources
            decision9()





        if decision <= 0 or decision >= 10:
            print("\n----> ERROR ..... That option is not available from the menu. Please pick one that is available.\n")



