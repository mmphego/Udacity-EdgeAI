import cv2
import numpy as np


def processing(image, height, width):
    resized_image = cv2.resize(image, (width, height))
    transposed_image = resized_image.transpose((2, 0, 1))
    reshaped_image = transposed_image.reshape(1, 3, height, width)
    return reshaped_image


def pose_estimation(input_image):
    """
    Given some input image, preprocess the image so that
    it can be used with the related pose estimation model
    you downloaded previously. You can use cv2.resize()
    to resize the image.

    Dimensions from: https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html
    """
    preprocessed_image = np.copy(input_image)
    # TODO: Preprocess the image for the pose estimation model
    preprocessed_image = processing(preprocessed_image, 256, 456)

    return preprocessed_image


def text_detection(input_image):
    """
    Given some input image, preprocess the image so that
    it can be used with the related text detection model
    you downloaded previously. You can use cv2.resize()
    to resize the image.

    Dimensions from: http://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html
    """
    preprocessed_image = np.copy(input_image)
    # TODO: Preprocess the image for the text detection model
    preprocessed_image = processing(preprocessed_image, 768, 1280)

    return preprocessed_image


def car_meta(input_image):
    """
    Given some input image, preprocess the image so that
    it can be used with the related car metadata model
    you downloaded previously. You can use cv2.resize()
    to resize the image.


    Dimensions from: https://docs.openvinotoolkit.org/latest/_models_intel_vehicle_attributes_recognition_barrier_0039_description_vehicle_attributes_recognition_barrier_0039.html
    """
    preprocessed_image = np.copy(input_image)
    # TODO: Preprocess the image for the car metadata model
    preprocessed_image = processing(preprocessed_image, 72, 72)

    return preprocessed_image
