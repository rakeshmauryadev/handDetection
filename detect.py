import cvzone
import cv2
import time

cap = cv2.VideoCapture(1)
detector = cvzone.HandDetector(maxHands=1, detectionCon=0.7)
mySerial = cvzone.SerialObject("COM3", 9600, 1)

while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    if lmList :
        fingers = detector.fingersUp()
        mySerial.sendData(fingers)
        print(fingers)

    cv2.imshow("Image", img)
    cv2.waitKey(1)