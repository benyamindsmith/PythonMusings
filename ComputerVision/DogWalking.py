## Detect Human Walking Dog
import cv2
frameWidth = 1024
frameHeight = 768


cap = cv2.VideoCapture("WalkingDog.mp4")

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodyCas = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    bodies = bodyCas.detectMultiScale(imgGray, 1.1,5)
    for x, y, w, h in bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Human", (x + (w // 2) - 30, y + (h // 2) - 30), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                    (0, 255, 0), 2)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
