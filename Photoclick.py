import cv2
cap = cv2.VideoCapture(0)
while True:
    status , photo =cap.read()
    status
    cv2.imshow("Hii Manoj ",photo)
    if cv2.waitKey() ==13:
      break