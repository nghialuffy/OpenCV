import cv2
import numpy as np

def AddWord(str,pic):
    font                   = cv2.FONT_HERSHEY_COMPLEX_SMALL
    bottomLeftCornerOfText = (0,50)
    fontScale              = 2
    fontColor              = (0,0,0)
    lineType               = 2

    cv2.putText(pic,str,
        bottomLeftCornerOfText,
        font,
        fontScale,
        fontColor,
        lineType)

def PurPose(pic):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (pic.shape[0]//2+35,pic.shape[1]//2-60)
    fontScale              = 2
    fontColor              = (0,0,0)
    lineType               = 3

    cv2.putText(pic,"[ ]",
        bottomLeftCornerOfText,
        font,
        fontScale,
        fontColor,
        lineType)

def FindColor (hsv):
    rong = hsv.shape[0]//2
    cao = hsv.shape[1]//2
    ###white
    min_white = np.array([70,15,210])
    max_white = np.array([100,55,255])
    ###green
    min_green = np.array([50,140,120])
    max_green = np.array([80,180,150])
    ###yellow
    min_yellow = np.array([10,180,190])
    max_yellow = np.array([40,230,220])
    ###black
    min_black = np.array([60,40,0])
    max_black = np.array([140,130,80])
    ###red
    min_red = np.array([0,140,150])
    max_red = np.array([255,180,190])

    mask = cv2.inRange(hsv, min_white, max_white)
    if(mask[rong,cao]==255):
        return "WHITE"
    mask = cv2.inRange(hsv, min_green, max_green)
    if(mask[rong,cao]==255):
        return "GREEN"
    mask = cv2.inRange(hsv, min_yellow, max_yellow)
    if(mask[rong,cao]==255):
        return "YELLOW"
    mask = cv2.inRange(hsv, min_black, max_black)
    if(mask[rong,cao]==255):
        return "BLACK"
    mask = cv2.inRange(hsv, min_red, max_red)
    if(mask[rong,cao]==255):
        return "RED"

vd = cv2.VideoCapture(0)
while(True):
    ret , frame = vd.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    AddWord(FindColor(hsv),frame)

    PurPose(frame)
    frame[frame.shape[0]//2,frame.shape[1]//2]=[255,22,3]
    cv2.imshow('frame', frame)
    print(hsv[hsv.shape[0]//2,hsv.shape[1]//2])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

