import time

import cv2
import pyautogui
import numpy as np
import threading

# Set the screen resolution
screen_width, screen_height = pyautogui.size()

# Set the output video dimensions and frame rate
output_width, output_height = screen_width, screen_height
fps = 20

# Create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output_video.avi", fourcc, fps, (output_width, output_height))

# Function to record the screen
def record_screen():
    while recording:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

# Start recording thread
recording = True
record_thread = threading.Thread(target=record_screen)
record_thread.start()

# Execute your code here
print('abcd')
time.sleep(5)


# Stop recording
recording = False
record_thread.join()

# Release the VideoWriter object and close windows
out.release()
cv2.destroyAllWindows()
