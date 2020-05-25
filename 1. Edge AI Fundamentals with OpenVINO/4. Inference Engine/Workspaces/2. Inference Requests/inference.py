import argparse
import cv2
from helpers import load_to_IE, preprocessing


CPU_EXTENSION = "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"


def get_args():
    """
    Gets the arguments from the command line.
    """
    parser = argparse.ArgumentParser("Load an IR into the Inference Engine")
    # -- Create the arguments
    parser.add_argument("-m", help="The location of the model XML file")
    parser.add_argument("-i", help="The location of the image input")
    parser.add_argument(
        "-r", help="The type of inference request: Async ('A') or Sync ('S')"
    )
    args = parser.parse_args()

    return args


def async_inference(exec_net, input_blob, image):
    """Code examples: https://docs.openvinotoolkit.org/latest/_inference_engine_ie_bridges_python_docs_api_overview.html
    """
    ### TODO: Add code to perform asynchronous inference
    exec_net.requests[0].async_infer({input_blob: image})
    exec_net.requests[0].wait()
    ### Note: Return the exec_net
    return exec_net


def sync_inference(exec_net, input_blob, image):
    ### TODO: Add code to perform synchronous inference
    res = exec_net.infer({input_blob: image})
    ### Note: Return the result of inference
    return res


def perform_inference(exec_net, request_type, input_image, input_shape):
    """
    Performs inference on an input image, given an ExecutableNetwork
    """
    # Get input image
    image = cv2.imread(input_image)
    # Extract the input shape
    n, c, h, w = input_shape
    # Preprocess it (applies for the IRs from the Pre-Trained Models lesson)
    preprocessed_image = preprocessing(image, h, w)

    # Get the input blob for the inference request
    input_blob = next(iter(exec_net.inputs))

    # Perform either synchronous or asynchronous inference
    request_type = request_type.lower()
    if request_type == "a":
        output = async_inference(exec_net, input_blob, preprocessed_image)
    elif request_type == "s":
        output = sync_inference(exec_net, input_blob, preprocessed_image)
    else:
        print("Unknown inference request type, should be 'A' or 'S'.")
        exit(1)

    # Return the exec_net for testing purposes
    return output


def main():
    args = get_args()
    exec_net, input_shape = load_to_IE(args.m, CPU_EXTENSION)
    perform_inference(exec_net, args.r, args.i, input_shape)


if __name__ == "__main__":
    main()
