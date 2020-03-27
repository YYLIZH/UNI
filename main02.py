import videoinput
import videoprocess
import cv2
import os
import numpy as np
import object_track
import queue
import process
import threading

leftupPos = [61, 123]
rightdownPos = [867, 578]
q1 = queue.Queue()
q2 = queue.Queue()

os.system('pause')


def run(leftupPos, rightdownPos, q1):
    x = rightdownPos[0] - leftupPos[0]
    y = rightdownPos[1] - leftupPos[1]
    New_leftupPos = [leftupPos[0] + int(x * 77 / 722), leftupPos[1] + int(y * 48 / 406)]
    New_rightdownPos = [rightdownPos[0] - int(x * 153 / 722), rightdownPos[1] - int(y * 169 / 406)]

    imgdect = videoinput.windowCapture(New_leftupPos, New_rightdownPos)
    im, imgray, position = videoprocess.find_note(imgdect)
    objList=[]
    for i in position:
        obj = object_track.note()
        obj.construct(i)
        obj.note_classify(imgray)
        objList.append(obj)
    Notelist=object_track.notelist()
    Notelist.update(objList, imgray)


    while True:
        imgdect = videoinput.windowCapture(New_leftupPos, New_rightdownPos)
        im, imgray, position = videoprocess.find_note(imgdect)

        objList = []
        for i in position:
            obj = object_track.note()
            obj.construct(i)
            obj.note_classify(imgray)
            objList.append(obj)
        Notelist = object_track.notelist()
        Notelist.update(objList, imgray)

        evoke_note = Notelist.evoke(imgray, im.shape[0])
        q1.put(evoke_note)
        q1.task_done()

        cv2.imshow('imm', im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    #return Notelist.list, New_rightdownPos[1]


run_thread = threading.Thread(target=run, args=(leftupPos, rightdownPos, q1,))
keyboard_thread = threading.Thread(target=process.keyboard, args=(q1, q2,))
collector_thread = threading.Thread(target=process.collector, args=(q2,))








'''
print(len(a))
for i in range(len(a)):
    print(a[i].position, a[i].property)

print(pos)
'''

