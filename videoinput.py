import win32gui
import win32ui
import win32con
import cv2
import numpy as np



def windowCapture(leftupPos,rightdownPos):

    hwnd = 0
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    w = rightdownPos[0]-leftupPos[0]
    h = rightdownPos[1]-leftupPos[1]
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, leftupPos, win32con.SRCCOPY)
    # dataBitMap.SaveBitmapFile(cDC, 'bmpfilenamename.jpg')
    # https://stackoverflow.com/questions/40306865/converting-a-winapi-screenshot-to-a-opencv-compatible-form
    # Free Resources
    im = dataBitMap.GetBitmapBits(False)
    img = np.array(im).astype(dtype="uint8")
    img = np.reshape(img, (h, w, 4))
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)


    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return img





