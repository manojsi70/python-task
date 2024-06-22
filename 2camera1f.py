import cv2

def main():
    # Capture from two cameras
    cap1 = cv2.VideoCapture(0)  # Change 0 to 1 if you have multiple cameras
    cap2 = cv2.VideoCapture(1)  # Change 1 to the second camera index

    if not cap1.isOpened() or not cap2.isOpened():
        print("Error: Could not open one or both cameras.")
        return

    while True:
        # Capture frame-by-frame
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("Error: Could not read frames from one or both cameras.")
            break

        # Resize the frames to the same size
        frame1 = cv2.resize(frame1, (640, 480))
        frame2 = cv2.resize(frame2, (640, 480))

        # Concatenate the frames horizontally
        combined_frame = cv2.hconcat([frame1, frame2])

        # Display the resulting frame
        cv2.imshow('Combined Frame', combined_frame)

        # Press 'q' on the keyboard to exit the loop
        if cv2.waitKey(1) ==13:
            break

    # When everything is done, release the capture
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
