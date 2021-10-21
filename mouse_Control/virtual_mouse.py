import time

import autopy
import cv2 as cv
import numpy as np

from Hand_Movement_Tracking import Hand_Movement_Tracking as hTrack

wCam, hCam = 720, 720
frameR = 75  # For the frame Reduction
smoothening = 8

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = hTrack()
wScr, hScr = autopy.screen.size()

while True:
    #  Find hand gestures
    success, img = cap.read()
    img = detector.findHands(img)
    lmks_lst, bbox = detector.findPosition(img)

    #  Get the tip of the index and middle finger in the array
    if len(lmks_lst) != 0:
        x1, y1 = lmks_lst[8][1:]
        x2, y2 = lmks_lst[12][1:]
        print(x1, y1, x2, y2)

        #  Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 150, 183), 2)

        #  Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            #  Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            #  Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            #  Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv.circle(img, (x1, y1), 15, (255, 150, 183), cv.FILLED)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:

            # Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # print(length)

            #  Click mouse if distance short
            if length < 40:
                cv.circle(img, (lineInfo[4], lineInfo[5]),
                          15, (0, 255, 0), cv.FILLED)
                autopy.mouse.click()

    #  It gave the frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (20, 50), cv.FONT_HERSHEY_PLAIN, 3,
               (255, 0, 0), 3)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
