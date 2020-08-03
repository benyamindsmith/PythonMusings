## Just a classic application of the body detection machine learning Algorithm to a crowd video 

import cv2
frameWidth = 1024
frameHeight = 768


cap = cv2.VideoCapture("Crowd.mp4")

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodyCas = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    bodies = bodyCas.detectMultiScale(imgGray, 1.1,1)
    for x, y, w, h in bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
