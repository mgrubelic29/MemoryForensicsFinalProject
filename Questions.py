

    questions = {
        "\n1. Out of these commands which is a volatiltiy plug-in?\n\ta) cd\n\tb) strings\n\tc) pslists\n\td) ipconfing" : "c",
        "\n2. What does pslsits do in volatiltiy?\n\ta) list all the processes of the system\n\tb) shows the name of the system\n\tc) prints a list of handles" : "a",
        "\n3. What is a PID?\n\ta) A PID helps identifies ip addresses.\n\tb) A PID is the ID number of a process.\n\tc) PID stands for Program In Domain.\n\td) PID's allows to search specific hives." : "b",
        "\n4. On a Pslist what helps you find previous processes that loads a current one?\n\ta) threads\n\tb) handles\n\tc) PID\n\td) PPID" : "d",
        "\n5. What does it mean if a process's handle and thread is 0?\n\ta) the process exists in another system?\n\tb) the process is not active, and may have been terminated\n\tc) that the process has been moved to another hive" : "b"
  	"n6. What plug-in do you use to find hidden processes?\n\ta) pslist\n\tb) pstree\n\tc) psscan\n\td) handles" : "c", 
	"n7. How does psscan view hidden processes?\n\ta) psscan uses pool tag scanning\n\tb) psscan uses hive tag scanning\n\tc) psscan scans through the hardware" : "a", 
	"n8. What is the downside of psscan?\n\ta) it doesn't have threads in the output\n\tb) it is still a possibility that all the processes is not shown\n\tc) the PPID could lead to a false process" : "b",
	"n9. What plug-in gives you a summary of the memory that is being analyzed?\n\ta)hivescan\n\tb)hiveslist\n\tc)imageinfo\n\td)iehistory" : "c", 
	"n10. What are one of things you can find in an imageinfo output?\n\ta) profiles\n\tb) ip address\n\tc) computer name\n\td) open sockets" : "a", 
	"n11. With imageinfo you can find the hardware architecture\n\ta) True\n\tb) false" : "True", 
	"n12. In an imageinfo output what does it mean when there is multiple KCPR addresses?\n\ta) that there's multiple service packs\n\tb) that there's malware hidden in memory\n\tc) that there's multiple profiles\n\td) that there's multiple processors" : "d", 
	"n13. What plug-in allows you to see the input and output that was on the command prompt? \n\ta)cmdscan\n\tb)consoles\n\tc)connscan" : "b", 
	"n14. With consoles you can see the aliases associated with the commands executed.\n\ta) True\n\tb) False" : "True", 
	"n15. Consoles cannot print the name and pid of attatched processes.\n\ta) True\n\tb) False" : "False", 
	"n16. Connections prints all TCP connections that were active during memory acquistion.\n\ta) True\n\tb) False" : "True", 
	"n17. Connections has the ability to can view nonactive connections.\n\ta) True\n\tb) False" : "False", 
	"n18. What plug-in allows to see active and non-active connections?\n\ta)connections\n\tb)sockscan\n\tc)connscan\n\td)sockets" : "c", 
	"n19. What plug-in finds listeners and endpoints from TCP's and UDP's?\n\ta)sockscan\n\tb)netscan\n\tc)hivescan\n\td)connscan" : "b",
	"n20. What Windows system is netscan NOT used for?\n\ta) Windows Vista\n\tb) Windows 2008 \n\tc) Windows XP use\n\td) Windows 7" : "c", 
	"n21. To find the physical addresses of registry hives in memory use ____\n\ta) hivescan\n\tb) privs\n\tc) printkey\n\td) imageinfo" : "a", 
	"n22. What makes hivescan hard to use?\n\ta) It only shows the PID's.\n\tb) It only shows the physical address of the hives.\n\tc) it only shows the physical address of the keys." : "b", 
	"n23. What plug-in is a better version of hivescan\n\ta) printkey\n\tb) yarascan\n\tc) hiveslist\n\td) pslist" : "c", 
	"n24. What does hivelist do?\n\ta) hivelist gives you the physical address \n\tb) hiveslist gives you the virtual address\n\tc) hiveslist gives you the full paths to certain hives.'\n\td) all the above" : "d", 
	"n25. Hiveslist prints the keys that are in memory.\n\ta) True\n\tb) False" : "False", 
	"n26. In order to look within the keys use the plug-in___\n\ta) hivelist\n\tb) privs\n\tc) printkey" : "c", 
	"n27. printkey allows to display the subkeys, values, and data that are in register keys.\n\ta) True \n\tb) False" : "True", 
	"n28. With printkey you can look into specific keys that will aid you in your investigation.\n\ta) True\n\tb) False" : "True", 
	"n29. What plug-in do you use to extract and decrypt domain credentials stored in registry\n\ta) memdump\n\tb) hashdump\n\tc) procdump\n\td) all the above" : "b", 
	"n30. What two virtual address does hashdump need to work?\n\ta) the virtual address of the ntuser.dat hive and SAM hive\n\tb) the virtual address of the SYSTEM hive and the SAM hive\n\tc) the virtual address of the HARDWARE hive and the DEFAULT hive\n\td) both b and c" : "b",  
	"n31. Once the hash is dumped, what can use the hashes for?\n\ta) find the password\n\tb) find the computer history\n\tc) find the malware" : "a", 
	"n32. the hashdump will still work even if a registry key isn't available in memory.\n\ta) True\n\tb) False" : "False",
	"n33. What plug-in allows you to see privileges ?\n\ta) privs\n\tb) iehistory\n\tc) privilege" : "a", 
	"n34. a privilege is the the permission or authority that process may have to do something in memory\n\ta)True\n\tb)False" : "True:, 
	"n35. The ____ flag makes privs only show the privilieges of processes that weren't enabled by default\n\ta) --enable\n\tb) --profile\n\tc) --silent\n\td) --less" : "c", 
	"n36. What flag do you use if you want see the list of plug-ins available\n\ta)-v\n\tb)-h\n\tc)-s" : "b", 
	"n37. Before using volatility you need the memory dump file that you want to analyze. What flag do you use
to get volatility to analyze the file \n\ta) -f\n\tb) -p\n\tc) -d\n\td) -m" : "a", 
	"n38. Before working with registers you need the flag --profile to implement a profile\n\ta) True\n\tb) False" : "True", 
	"n39. What flag do you use before looking into a key when working with printkey\n\ta) -h\n\tb) -s\n\tc) -k" : "c", 
	"n40. When you use hashdump you need the physical address of the SYSTEM hive and SAM hive.
The flag -s is for the SYSTEM and -y for SAM.\n\ta) True\n\tb) False; -y is for SYSTEM and -s is for SAM" : "False", 
	"n41. How do you analyze specefic processes?\n\ta) only use the flag -p\n\tb) use the flag -p then input the PID of the certain processes\n\tc) just put in the PID of the process you want to analyze" : "b", 
	"n42. What are registry keys?\n\ta) it is what carries all the data about the system \n\tb) only carries data about hardware\n\tc) only carries data about the processes" : "a", 
	"n43. What is volatility?\n\ta) a memory forensics plug-in\n\tb) a private memory forensics framework\n\tc) a open-source memory forensics framework" : "c", 

  }

    