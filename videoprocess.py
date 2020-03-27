import cv2
import numpy as np


def find_note(im):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    imsharpen = cv2.filter2D(im, -1, kernel)
    imgray_sharp = cv2.cvtColor(imsharpen, cv2.COLOR_BGR2GRAY)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray_sharp, 127, 255, 0)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    AreaPropotion = im.shape[0] * im.shape[1] / 104895
    X_Propotion = im.shape[0] / 185
    Y_Propotion = im.shape[1] / 567
    positionList = np.array([], dtype=int)
    for cnt in contours:
        cntList = []
        if len(cnt) <= 100 and len(cnt) >= 6:
            area = cv2.contourArea(cnt)
            if area > 200 * AreaPropotion and area < 1000 * AreaPropotion:

                cntList.extend(cnt)
                cntList = np.array(cntList)
                x = int((max(cntList[:, 0][:, 0]) + min(cntList[:, 0][:, 0])) / 2)
                x_diff = int(max(cntList[:, 0][:, 0]) - min(cntList[:, 0][:, 0]))
                y = int((max(cntList[:, 0][:, 1]) + min(cntList[:, 0][:, 1])) / 2)
                y_diff = int(max(cntList[:, 0][:, 1]) - min(cntList[:, 0][:, 1]))
                if abs(x_diff - y_diff) < 2 * min(x_diff, y_diff):
                    cv2.drawContours(im, [cnt], 0, (0, 0, 255), 2)
                    positionList = np.append(positionList, [x, y, min(cntList[:, 0][:, 1]), None])
                    positionList = positionList.reshape(-1, 4)
                    positionList = matrix_radix_sort(positionList)
                    hold = positionList[0, 0]
                    cv2.circle(im, (positionList[0, 0], positionList[0, 1]), 2, (0, 0, 255), 0)
                    curr = 1
                    tail = len(positionList)
                    while tail - curr > 0:
                        if abs(hold - positionList[curr, 0]) < 10:
                            positionList = np.delete(positionList, (curr), axis=0)
                            tail = tail - 1
                        else:
                            hold = positionList[curr, 0]
                            cv2.circle(im, (positionList[curr, 0], positionList[curr, 1]), 2, (0, 0, 255), 0)
                            curr = curr + 1

    for i in range(len(positionList)):
        positionList[i] = classify(positionList[i], imgray)

    return im, imgray, positionList


def matrix_radix_sort(matrix):
    matrix = matrix[matrix[:, 1].argsort()]
    hold = 0
    for i in range(len(matrix[:, 1])):
        if matrix[i, 1]!=hold:
            result = np.where(matrix[:, 1] == matrix[i, 1])
            if len(result[0]) > 1:
                order=result[0]
                matrix[order] = matrix[order][matrix[order][:, 0].argsort()]
            hold = matrix[i, 1]
    return matrix


def classify(array, imgray):
    for i in range(array[1], array[2]-3, -1):
        if imgray[i][array[0]] < 120:
            array[3] = 1
            return array
        else:
            array[3] = 0
    return array



