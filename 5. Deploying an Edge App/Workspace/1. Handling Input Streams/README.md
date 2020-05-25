# Handling Input Streams

It's time to really get in the think of things for running your app at the edge. Being able to
appropriately handle an input stream is a big part of having a working AI or computer vision
application. 

In your case, you will be implementing a function that can handle camera, video or webcam
data as input. While unfortunately the classroom workspace won't allow for webcam usage,
you can also try that portion of your code out on your local machine if you have a webcam
available.

As such, the tests here will focus on using a camera image or a video file. You will not need to
perform any inference on the input frames, but you will need to do a few other image
processing techniques to show you have some of the basics of OpenCV down.

Your tasks are to:

1. Implement a function that can handle camera image, video file or webcam inputs
2. Use `cv2.VideoCapture()` and open the capture stream
3. Re-size the frame to 100x100
4. Add Canny Edge Detection to the frame with min & max values of 100 and 200, respectively
5. Save down the image or video output
6. Close the stream and any windows at the end of the application

You won't be able to test a webcam input in the workspace unfortunately, but you can use
the included video and test image to test your implementations.
