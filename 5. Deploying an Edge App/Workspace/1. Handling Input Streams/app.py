import argparse
import cv2
import numpy as np
from tqdm import tqdm


def get_args():
    """Gets the arguments from the command line."""
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"
    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args


def capture_stream(args):
    ### TODO: Handle image, video or webcam
    image_flag = False
    if args.i == "CAM":
        args.i = 0
    elif args.i.endswith((".jpg", "png", ".bmp")):
        image_flag = True

    ### TODO: Get and open video capture
    stream_capture = cv2.VideoCapture(args.i)
    stream_capture.open(args.i)

    new_width, new_height = 100, 100

    # width, height = stream_capture.get(3), stream_capture.get(4)

    out = None
    if not image_flag:
        # To write to mp4 you would need to used MP4 Codecs
        # See: https://stackoverflow.com/questions/30103077/what-is-the-codec-for-mp4-videos-in-python-opencv
        # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#saving-a-video
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter("out.mp4", fourcc, 30, (new_width, new_height))

    length = stream_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = stream_capture.get(cv2.CAP_PROP_FPS)
    pbar = tqdm(total=int(length - fps + 1))

    while stream_capture.isOpened():
        pbar.update(1)
        flag, frame = stream_capture.read()
        if not flag:
            break
        # Easily exit from opencv
        key_pressed = cv2.waitKey(60)

        ### TODO: Re-size the frame to 100x100
        frame = cv2.resize(frame, (new_width, new_height))
        ### TODO: Add Canny Edge Detection to the frame,
        ###       with min & max values of 100 and 200
        frame = cv2.Canny(frame, 100, 200)
        ###       Make sure to use np.dstack after to make a 3-channel image
        frame = np.dstack((frame,) * 3)

        ### TODO: Write out the frame, depending on image or video
        if image_flag:
            cv2.imwrite("output_image.jpg", frame)
        else:
            out.write(frame)

        if key_pressed == 27:
            break

    ### TODO: Close the stream and any windows at the end of the application
    pbar.close()
    if not image_flag:
        out.release()
    stream_capture.release()
    cv2.destroyAllWindows()


def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
