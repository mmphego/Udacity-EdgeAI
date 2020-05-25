# Convert a TensorFlow Model

In this exercise, you'll convert a TensorFlow Model from the Object Detection Model Zoo
into an Intermediate Representation using the Model Optimizer.

As noted in the related [documentation](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html), 
there is a difference in method when using a frozen graph vs. an unfrozen graph. Since
freezing a graph is a TensorFlow-based function and not one specific to OpenVINO itself,
in this exercise, you will only need to work with a frozen graph. However, I encourage you to
try to freeze and load an unfrozen model on your own as well.

For this exercise, first download the SSD MobileNet V2 COCO model from [here](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz). Use the `tar -xvf` 
command with the downloaded file to unpack it.

From there, find the **Convert a TensorFlow\* Model** header in the documentation, and
feed in the downloaded SSD MobileNet V2 COCO model's `.pb` file. 

If the conversion is successful, the terminal should let you know that it generated an IR model.
The locations of the `.xml` and `.bin` files, as well as execution time of the Model Optimizer,
will also be output.

**Note**: Converting the TF model will take a little over one minute in the workspace.

### Hints & Troubleshooting

Make sure to pay attention to the note in this section regarding the 
`--reverse_input_channels` argument. 
If you are unsure about this argument, you can read more [here](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_Converting_Model_General.html#when_to_reverse_input_channels).

There is additional documentation specific to converting models from TensorFlow's Object
Detection Zoo [here](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_tf_specific_Convert_Object_Detection_API_Models.html).
You will likely need both the `--tensorflow_use_custom_operations_config` and
`--tensorflow_object_detection_api_pipeline_config` arguments fed with their 
related files.

