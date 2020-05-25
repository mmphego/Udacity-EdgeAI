# Convert an ONNX Model - Solution

First, you can start by checking out the documentation specific to ONNX models [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_ONNX.html).

Now, given that I was in the directory with the ONNX model file, here was the 
full path to convert my model:

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model model.onnx
```
