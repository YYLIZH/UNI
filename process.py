import threading
import time
import numpy
import queue


def emitter_machine(q1):
    while True:
        q1.put()
        q1.task_done()


class Buffer:
    def delay(self, note):
        time.sleep(3)
        return note


def keyboard(q1, q2):
    while True:
        delay_noteList=[]
        for i in range(len(q1.get)):
            b = Buffer()
            delay_noteList.append(b.delay(q1.get[i]))
        q2.put(delay_noteList)


def collector(q2):
    while True:
        print(q2.get())
        q2.task_done()