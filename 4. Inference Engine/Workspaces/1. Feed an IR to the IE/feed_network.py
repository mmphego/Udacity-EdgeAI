import argparse
### TODO: Load the necessary libraries
from pathlib import Path
from openvino.inference_engine import IENetwork, IECore, IEPlugin

CPU_EXTENSION = "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Load an IR into the Inference Engine")
    # -- Create the descriptions for the commands
    m_desc = "The location of the model XML file"

    # -- Create the arguments
    parser.add_argument("-m", help=m_desc)
    args = parser.parse_args()

    return args


def load_to_IE(model_xml):
    # See: https://docs.openvinotoolkit.org/latest/_inference_engine_ie_bridges_python_docs_api_overview.html
    ### TODO: Load the Inference Engine API

    ie = IECore()

    ### TODO: Load IR files into their related class
    model_xml_path = Path(model_xml)
    if model_xml_path.exists():
        model_bin_path = model_xml_path.absolute()
        model_bin_path = Path(model_bin_path.as_posix().replace('xml', 'bin'))
        assert model_bin_path.is_file()

    net = IENetwork(model=str(model_xml), weights=str(model_bin_path))
    ### TODO: Add a CPU extension, if applicable. It's suggested to check
    ###       your code for unsupported layers for practice before
    ###       implementing this. Not all of the models may need it.
    #
    ie.add_extension(extension_path=CPU_EXTENSION, device_name='CPU' )
    ### TODO: Get the supported layers of the network
    #plugin = IEPlugin(device='CPU')
    #print(plugin.get_supported_layers(net))
    supported_layers = ie.query_network(network=net, device_name='CPU')
    #print(supported_layers)
    ### TODO: Check for any unsupported layers, and let the user
    ###       know if anything is missing. Exit the program, if so.
    unsupported_layers = [l for l in net.layers.keys() if l not in supported_layers]
    if len(unsupported_layers) != 0:
        print("Unsupported layers found: {}".format(unsupported_layers))
        print("Check whether extensions are available to add to IECore.")
        exit(1)

    ### TODO: Load the network into the Inference Engine
    ie.load_network(net, "CPU")
    print("IR successfully loaded into Inference Engine.")

    return ie


def main():
    args = get_args()
    load_to_IE(args.m)


if __name__ == "__main__":
    main()
