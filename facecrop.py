import cv2
def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from the camera.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Crop and display the faces
        for x, y, w, h in faces:
            cropped_face = frame[y : y + h, x : x + w]
            cv2.imshow("Cropped Face", cropped_face)

        # Show the main frame with detected faces
        cv2.imshow("Main Frame", frame)

        # Press 'q' on the keyboard to exit the loop
        if cv2.waitKey(1) == 13:
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
