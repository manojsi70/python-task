import cv2

def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    # Load the overlay images
    sunglasses = cv2.imread('sunglasses.png')
    stars = cv2.imread('stars.png')

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from the camera.")
            break

        # Overlay sunglasses on the frame
        frame[50:50+sunglasses.shape[0], 150:150+sunglasses.shape[1]] = sunglasses

        # Overlay stars on the frame
        frame[200:200+stars.shape[0], 50:50+stars.shape[1]] = stars

        # Display the resulting frame
        cv2.imshow('Filtered Image', frame)

        # Press 'q' on the keyboard to exit the loop
        if cv2.waitKey(1) & 0xFF == 13:
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
