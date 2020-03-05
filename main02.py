import videoinput
import videoprocess
import cv2
import os
import numpy as np
import object_track

def run(leftupPos, rightdownPos):
    x = rightdownPos[0] - leftupPos[0]
    y = rightdownPos[1] - leftupPos[1]
    New_leftupPos = [leftupPos[0] + int(x * 77 / 722), leftupPos[1] + int(y * 48 / 406)]
    New_rightdownPos = [rightdownPos[0] - int(x * 153 / 722), rightdownPos[1] - int(y * 169 / 406)]

    imgdect = videoinput.windowCapture(New_leftupPos, New_rightdownPos)
    _,position = videoprocess.find_note(np.copy(imgdect))
    objList=[]
    for i in position:
        obj=object_track.note()
        obj.construct(i)
        objList.append(obj)
    Notelist=object_track.notelist()
    Notelist.add(objList)


    while True:
        imgdect = videoinput.windowCapture(New_leftupPos,New_rightdownPos)
        im, position = videoprocess.find_note(np.copy(imgdect))
        Notelist.update(position)
        cv2.imshow('imm', im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return Notelist.list

os.system('pause')
a = run([155, 272], [875, 676])
print(len(a))
