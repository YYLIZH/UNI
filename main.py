import setup
import pyautogui
import threading
import run
import os

dePosList, PosList, leftupPos, rightdownPos = setup.SystemSetup()
Pos1 = dePosList[0]
Pos2 = dePosList[1]
Pos3 = dePosList[2]
Pos4 = dePosList[3]
Pos5 = dePosList[4]


def a():
    run.detector("Pos1").check(pyautogui.Point(Pos1[0], Pos1[1]))


def b():
    run.detector("Pos2").check(pyautogui.Point(Pos2[0], Pos2[1]))


def c():
    run.detector("Pos3").check(pyautogui.Point(Pos3[0], Pos3[1]))


def d():
    run.detector("Pos4").check(pyautogui.Point(Pos4[0], Pos4[1]))


def e():
    run.detector("Pos5").check(pyautogui.Point(Pos5[0], Pos5[1]))


print("setup is ready")
os.system('pause')

'''
Processes = []
Processes.append(multiprocessing.Process(target=a.check(pyautogui.Point(Pos1[0], Pos1[1]))))
Processes.append(multiprocessing.Process(target=b.check(pyautogui.Point(Pos2[0], Pos2[1]))))
Processes.append(multiprocessing.Process(target=c.check(pyautogui.Point(Pos3[0], Pos3[1]))))
Processes.append(multiprocessing.Process(target=d.check(pyautogui.Point(Pos4[0], Pos4[1]))))
Processes.append(multiprocessing.Process(target=e.check(pyautogui.Point(Pos5[0], Pos5[1]))))
for process in Processes:
    process.start()
'''

threads = []
threads.append(threading.Thread(target=a))
threads.append(threading.Thread(target=b))
threads.append(threading.Thread(target=c))
threads.append(threading.Thread(target=d))
threads.append(threading.Thread(target=e))
for t in threads:
    t.start()




