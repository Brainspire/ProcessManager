import os,sys,random

from classes.proc import Proc

strCurrentDir = os.path.dirname(os.path.abspath(__file__))

dicProcesses = {}
for i in range(5):
    dicProcesses["process" + str(i)] = ["python3", os.path.join(strCurrentDir, "test.py"), str(random.randint(2, 10))]

objPrcessManager = Proc()
objPrcessManager.run(dicProcesses)
print(objPrcessManager.getProcessData("process2"))
