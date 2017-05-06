# Read a video file frame by frame, counting all occurrences of colors

import numpy as np
import time
import cv2

# Return a 3d array of ints, counting each occurrence of a pixel of that RGB
def bucketize(fileName):
    cap = cv2.VideoCapture( fileName )
    w = int(cap.get(3))  # get width, cap attribute 3
    h = int(cap.get(4))  # get height, cap attribute 4
    frameCount = 0
    pixCount   = 0
    start = time.time()

    # 3d int array corresponding to RGB values
    bucket = np.zeros((256, 256, 256))

    # Get the first frame, if it exists
    ret, frame = cap.read()

    # Read all frameCount, put their colors into buckets
    while(ret):
        # This kills the runtime
        for row in frame:
            for px in row:
                pixCount += 1
                # Add the colors to the bucket
                bucket[ px[0] ] [ px[1] ] [ px[2] ] += 1


        # Capture frame-by-frame
        ret, frame = cap.read()

        # Count frameCount
        frameCount+=1

    # For time elapse calculations
    end = time.time()
    pixels = w * h * frameCount

    # Some probably useless output
    print("Width: ", w)
    print("Height: ", h)
    print("Frames: ", frameCount)
    print("Process Time: ", end - start)
    print("Processed Pixels: ", pixels)

    s = "{:.3f} {:d} {:d} {:d} {:d} {:s}\n".format(end-start, w, h, frameCount, pixCount, fileName)
    # Append the elapsed time to timeLog.txt
    with open("timeLog.txt", "a") as f:
        # f.write( str(end - start) )
        # f.write( str(w) )
        # f.write( str(h) )
        # f.write( str(frameCount) )
        # f.write( '\n')
        f.write(s)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return bucket


bucket1 = bucketize("test1.webm")