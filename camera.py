#!/usr/bin/python3

import cv2
import cgi
import cgitb
import os

cgitb.enable()  # Enable debugging for CGI scripts

print("Content-Type: text/html\n")
print("<html><body>")
print("<h1>Control Camera</h1>")

# Try to open the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("<p>Failed to access the camera.</p>")
else:
    ret, frame = cap.read()
    cap.release()

    if ret:
        # Define the path to save the captured image
        image_path = '/path/to/your/cgi-bin/captured_image.jpg'
        cv2.imwrite(image_path, frame)

        # Make sure the image file exists
        if os.path.exists(image_path):
            print(f'<img src="/cgi-bin/captured_image.jpg" alt="Captured Image">')
        else:
            print("<p>Failed to save the captured image.</p>")
    else:
        print("<p>Failed to capture an image from the camera.</p>")

print("</body></html>")
