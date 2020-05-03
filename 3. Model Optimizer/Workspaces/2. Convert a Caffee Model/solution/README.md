# Convert a Caffe Model - Solution

First, you can start by checking out the documentation specific to Caffe models [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_Caffe.html).

I did notice an additional helpful argument here: `--input_proto`, which is used to specify
a `.prototxt` file to pair with the `.caffemodel` file when the model name and `.prototxt`
filename do not match.

Now, given that I was in the directory with the Caffe model file & `.prototxt` file, here was the full path to convert my model:

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model squeezenet_v1.1.caffemodel --input_proto deploy.prototxt
```
