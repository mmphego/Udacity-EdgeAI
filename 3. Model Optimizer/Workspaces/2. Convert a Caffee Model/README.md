# Convert a Caffe Model

In this exercise, you'll convert a Caffe Model into an Intermediate Representation using the Model Optimizer. You can find the related documentation [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_Caffe.html).

For this exercise, first download the SqueezeNet V1.1 model by cloning [this repository](https://github.com/DeepScale/SqueezeNet).

Follow the documentation above and feed in the Caffe model to the Model Optimizer.

If the conversion is successful, the terminal should let you know that it generated an IR model.
The locations of the `.xml` and `.bin` files, as well as execution time of the Model Optimizer,
will also be output.

### Hints & Troubleshooting

You will need to specify `--input_proto` if the `.prototxt` file is not named the same as the model.

There is an important note in the documentation after the section **Supported Topologies** 
regarding Caffe models trained on ImageNet. If you notice poor performance in inference, you
may need to specify mean and scale values in your arguments.

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model squeezenet_v1.1.caffemodel --input_proto deploy.prototxt
```
