# ProcessManager
Python 3.5 class to run processes in parallel

Written by Robert Baldessari

## Description
This is a simple Python class to run multiple processes in parallel. With this class you can pass in a list of commands you want to run as well as a concurrent limit on the number of processes to have running at any given time.

Simply instantiate the class while passing the concurrent limit to the constructor, call run with a dictionary of commands and then call getProcessData with the option of passing in one of the keys from the original dictionary of commands.

This has been tested with Python 3.5 and has no dependencies outside of the standard default libraries provided in Python 3.5.

## Installation
0. Download the repository
0. Add proc.py to your program

## Example Usage
	import os,random

	from classes.proc import Proc

	strCurrentDir = os.path.dirname(os.path.abspath(__file__))

	dicProcesses = {}
	for i in range(5):
		dicProcesses["process" + str(i)] = ["python3", os.path.join(strCurrentDir, "test.py"), str(random.randint(2, 10))]

	objPrcessManager = Proc()
	objPrcessManager.run(dicProcesses)
	print(objPrcessManager.getProcessData("process2"))

## Disclaimer
This software is provided as-is.  The author makes no guarantee to release an updated version to fix any incompatibilities.
