# Convert a TensorFlow Model - Solution

First, you can start by checking out the additional documentation specific to TensorFlow
models from the Model Detection Zoo [here](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_tf_specific_Convert_Object_Detection_API_Models.html).

I noticed three additional arguments that were important here:

- `--tensorflow_object_detection_api_pipeline_config`
- `--tensorflow_use_custom_operations_config`
- `--reverse_input_channels`

The first of these just needs the `pipeline.config` file that came with the downloaded model.

The second of these needs a JSON support file for TensorFlow models. I found that the
`ssd_v2_support.json` extension worked with the MobileNet model here.

The final of these is due to the TensorFlow models being trained on RGB images, but the
Inference Engine otherwise defaulting to BGR.

Now, given that I was in the directory with the frozen model file from TensorFlow, here was the 
full path to convert my model:

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json
```
