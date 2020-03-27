import os
import pyautogui
import cv2


print('Please resize the window as this cute Kawada picture')
img = cv2.imread('kawada.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


def SystemSetup():
    print('record the leftup position')
    os.system('pause')
    leftup = pyautogui.position()
    leftupPos = [leftup[0], leftup[1]]

    print('record the rightdown position')
    os.system('pause')
    rightdown = pyautogui.position()
    rightdownPos = [rightdown[0], rightdown[1]]

    x = rightdownPos[0]-leftupPos[0]
    y = rightdownPos[1]-leftupPos[1]

    shift = y*1.1/7
    Pos1 = [(leftupPos[0]+int(y*3.5/7)), (rightdownPos[1]-int(y*1.32/7+shift))]
    Pos2 = [(leftupPos[0]+int(y*5.4/7)), (rightdownPos[1]-int(y*1.29/7+shift))]
    Pos3 = [(leftupPos[0]+int(y*7.3/7)), (rightdownPos[1]-int(y*1.3/7+shift))]
    Pos4 = [(leftupPos[0]+int(y*9.1/7)), (rightdownPos[1]-int(y*1.28/7+shift))]
    Pos5 = [(leftupPos[0]+int(y*10.8/7)), (rightdownPos[1]-int(y*1.33/7+shift))]
    PosList = [Pos1, Pos2, Pos3, Pos4, Pos5]

    dePos1 = [Pos1[0]+int(y*40/406), Pos1[1]-int(y*90/406)]
    dePos2 = [Pos2[0]+int(y*21/406), Pos2[1]-int(y*129/406)]
    dePos3 = [Pos3[0],Pos3[1]-int(y*132/406)]
    dePos4 = [Pos4[0]-int(y*21/406),Pos4[1]-int(y*127/406)]
    dePos5 = [Pos5[0]-int(y*40/406),Pos5[1]-int(y*85/406)]

    dePosList = [dePos1, dePos2, dePos3, dePos4, dePos5]

    New_leftupPos = [leftupPos[0]+int(x*73/722), leftupPos[1]+int(y*117/407)]
    New_rightdownPos = [rightdownPos[0]-int(x*111/722), rightdownPos[1]-int(y*140/407)]
    return leftupPos, rightdownPos


leftupPos,  rightdownPos = SystemSetup()
print('The upper left position is: ', leftupPos)
print('\n')
print('The lower right position is: ', rightdownPos)

'''
PosList, dePosList, leftupPos, rightdownPos = SystemSetup()
pyautogui.click(dePosList[0])
'''
