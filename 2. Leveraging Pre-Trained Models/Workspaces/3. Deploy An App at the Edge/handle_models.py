import cv2
import numpy as np


def handle_pose(output, input_shape):
    """
    Handles the output of the Pose Estimation model.
    Returns ONLY the keypoint heatmaps, and not the Part Affinity Fields.

    From: https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html
    Inputs

        name: "input" , shape: [1x3x256x456] - An input image in the format [BxCxHxW], where:
            B - batch size
            C - number of channels
            H - image height
            W - image width. Expected color order is BGR.

    Outputs

        The net outputs two blobs with shapes: [1, 38, 32, 57] and [1, 19, 32, 57]. The first blob contains keypoint pairwise relations (part affinity fields), the second one contains keypoint heatmaps.

    """
    # TODO 1: Extract only the second blob output (keypoint heatmaps)
    heatmaps = output.get("Mconv7_stage2_L2")
    # TODO 2: Resize the heatmap back to the size of the input
    out_heatmap = np.zeros([heatmaps.shape[1], input_shape[0], input_shape[1]])
    for h in range(len(heatmaps[0])):
        out_heatmap[h] = cv2.resize(heatmaps[0][h], input_shape[0:2][::-1])

    return out_heatmap

def handle_text(output, input_shape):
    """
    Handles the output of the Text Detection model.
    Returns ONLY the text/no text classification of each pixel,
        and not the linkage between pixels and their neighbors.

    From: https://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html
    Inputs

        name: "input" , shape: [1x3x768x1280] - An input image in the format [BxCxHxW], where:
            B - batch size
            C - number of channels
            H - image height
            W - image width

        Expected color order - BGR.

    Outputs

        The net outputs two blobs. Refer to PixelLink and demos for details.
            [1x2x192x320] - logits related to text/no-text classification for each pixel.
            [1x16x192x320] - logits related to linkage between pixels and their neighbors.

    """
    # TODO 1: Extract only the first blob output (text/no text classification)
    pixellink = output.get('model/segm_logits/add')
    # TODO 2: Resize this output back to the size of the input
    out_text = np.empty([pixellink.shape[1], input_shape[0], input_shape[1]])
    for t in range(len(pixellink[0])):
        out_text[t] = cv2.resize(pixellink[0][t], input_shape[0:2][::-1])
    print(out_text.shape) #(1, 2, 192, 320)
    print(input_shape) # (1, 3, 768, 1280)
    # data = data.reshape((data.shape[0], data.shape[1], 1))

    return out_text


def handle_car(output, input_shape):
    """
    Handles the output of the Car Metadata model.
    Returns two integers: the argmax of each softmax output.
    The first is for color, and the second for type.

    From: https://docs.openvinotoolkit.org/latest/_models_intel_vehicle_attributes_recognition_barrier_0039_description_vehicle_attributes_recognition_barrier_0039.html

    Inputs

        name: "input" , shape: [1x3x72x72] - An input image in following format [1xCxHxW], where:

        - C - number of channels
        - H - image height
        - W - image width.

    Expected color order - BGR.

    Outputs

        name: "color", shape: [1, 7, 1, 1] - Softmax output across seven color classes [white, gray, yellow, red, green, blue, black]
        name: "type", shape: [1, 4, 1, 1] - Softmax output across four type classes [car, bus, truck, van]
    """
    color = output.get('color')
    output_type = output.get('type')
    # TODO 1: Get the argmax of the "color" output
    color = np.argmax(color)
    # TODO 2: Get the argmax of the "type" output
    output_type = np.argmax(output_type)

    return color, output_type


def handle_output(model_type):
    """
    Returns the related function to handle an output,
        based on the model_type being used.
    """
    if model_type == "POSE":
        return handle_pose
    elif model_type == "TEXT":
        return handle_text
    elif model_type == "CAR_META":
        return handle_car
    else:
        return None


"""
The below function is carried over from the previous exercise.
You just need to call it appropriately in `app.py` to preprocess
the input image.
"""


def preprocessing(input_image, height, width):
    """
    Given an input image, height and width:
    - Resize to width and height
    - Transpose the final "channel" dimension to be first
    - Reshape the image to add a "batch" of 1 at the start
    """
    image = np.copy(input_image)
    image = cv2.resize(image, (width, height))
    image = image.transpose((2, 0, 1))
    image = image.reshape(1, 3, height, width)

    return image
