import os
import cv2
import numpy as np
from openvino.inference_engine import IENetwork, IECore

'''
The below functions are carried over from previous exercises.
They are already called appropriately in inference.py.
'''
def load_to_IE(model_xml, cpu_extension):
    # Load the Inference Engine API
    plugin = IECore()

    # Load IR files into their related class
    model_bin = os.path.splitext(model_xml)[0] + ".bin"
    net = IENetwork(model=model_xml, weights=model_bin)

    # Add a CPU extension, if applicable.
    if cpu_extension:
        plugin.add_extension(cpu_extension, "CPU")

    # Get the supported layers of the network
    supported_layers = plugin.query_network(network=net, device_name="CPU")

    # Check for any unsupported layers, and let the user
    # know if anything is missing. Exit the program, if so.
    unsupported_layers = [l for l in net.layers.keys() if l not in supported_layers]
    if len(unsupported_layers) != 0:
        print("Unsupported layers found: {}".format(unsupported_layers))
        print("Check whether extensions are available to add to IECore.")
        exit(1)

    # Load the network into the Inference Engine
    exec_net = plugin.load_network(net, "CPU")

    # Get the input layer
    input_blob = next(iter(net.inputs))

    # Get the input shape
    input_shape = net.inputs[input_blob].shape

    return exec_net, input_shape


def preprocessing(input_image, height, width):
    '''
    Given an input image, height and width:
    - Resize to width and height
    - Transpose the final "channel" dimension to be first
    - Reshape the image to add a "batch" of 1 at the start 
    '''
    image = np.copy(input_image)
    image = cv2.resize(image, (width, height))
    image = image.transpose((2,0,1))
    image = image.reshape(1, 3, height, width)

    return image
