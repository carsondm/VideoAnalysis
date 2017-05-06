# Read a video file frame by frame, counting all occurrences of colors

import numpy as np
import time
import cv2

cap = cv2.VideoCapture('dance.webm')
w = cap.get(3)  # get width, cap attribute 3
h = cap.get(4)  # get height, cap attribute 4
frames = 0
start = time.time()

bucket = np.zeros((256, 256, 256))

# Get the first frame, if it exists
ret, frame = cap.read()

# Read all frames, put their colors into buckets
while(ret):
    # Count frames
    frames+=1

    # Print the top left pixel color channels (RGB)
    px = frame[0, 0]

    # Add the colors to the bucket
    bucket[px[0]][px[1]][px[2]] += 1

    # Capture frame-by-frame
    ret, frame = cap.read()

# For time elapse calculations
end = time.time()

# Some probably useless output
print("Width: ", w)
print("Height: ", h)
print("Frames: ", frames)
print("Process Time: ", end - start)

# Append the elapsed time to timeLog.txt
with open("timeLog.txt", "a") as f:
    s = str( end - start )
    f.write( s )
    f.write( '\n')

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
