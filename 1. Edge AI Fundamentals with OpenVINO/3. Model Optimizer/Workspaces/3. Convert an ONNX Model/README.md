# Convert an ONNX Model

### Exercise Instructions

In this exercise, you'll convert an ONNX Model into an Intermediate Representation using the 
Model Optimizer. You can find the related documentation [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_ONNX.html).

For this exercise, first download the bvlc_alexnet model from [here](https://s3.amazonaws.com/download.onnx/models/opset_8/bvlc_alexnet.tar.gz). Use the `tar -xvf` command with the downloaded file to unpack it.

Follow the documentation above and feed in the ONNX model to the Model Optimizer.

If the conversion is successful, the terminal should let you know that it generated an IR model.
The locations of the `.xml` and `.bin` files, as well as execution time of the Model Optimizer,
will also be output.

### PyTorch models

Note that we will only cover converting directly from an ONNX model here. If you are interested
in converting a PyTorch model using ONNX for use with OpenVINO, check out this [link](https://michhar.github.io/convert-pytorch-onnx/) for the steps to do so. From there, you can follow the steps in the rest
of this exercise once you have an ONNX model.
