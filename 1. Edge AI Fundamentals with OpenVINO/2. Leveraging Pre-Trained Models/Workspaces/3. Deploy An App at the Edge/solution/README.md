# Deploy Your First Edge App - Solution

## `handle_models.py`

First, let's look in `handle_models.py` for each handling of an output.

### `handle_pose`

```
def handle_pose(output, input_shape):
    '''
    Handles the output of the Pose Estimation model.
    Returns ONLY the keypoint heatmaps, and not the Part Affinity Fields.
    '''
    # TODO 1: Extract only the second blob output (keypoint heatmaps)
    heatmaps = output['Mconv7_stage2_L2']
    # TODO 2: Resize the heatmap back to the size of the input
    # Create an empty array to handle the output map
    out_heatmap = np.zeros([heatmaps.shape[1], input_shape[0], input_shape[1]])
    # Iterate through and re-size each heatmap
    for h in range(len(heatmaps[0])):
        out_heatmap[h] = cv2.resize(heatmaps[0][h], input_shape[0:2][::-1])

    return out_heatmap
```

### `handle_text`

```
def handle_text(output, input_shape):
    '''
    Handles the output of the Text Detection model.
    Returns ONLY the text/no text classification of each pixel,
    and not the linkage between pixels and their neighbors.
    '''
    # TODO 1: Extract only the first blob output (text/no text classification)
    text_classes = output['model/segm_logits/add']
    # TODO 2: Resize this output back to the size of the input
    out_text = np.empty([text_classes.shape[1], input_shape[0], input_shape[1]])
    for t in range(len(text_classes[0])):
        out_text[t] = cv2.resize(text_classes[0][t], input_shape[0:2][::-1])

    return out_text
```

### `handle_car`

```
def handle_car(output, input_shape):
    '''
    Handles the output of the Car Metadata model.
    Returns two integers: the argmax of each softmax output.
    The first is for color, and the second for type.
    '''
    # Get rid of unnecessary dimensions
    color = output['color'].flatten()
    car_type = output['type'].flatten()
    # TODO 1: Get the argmax of the "color" output
    color_pred = np.argmax(color)
    # TODO 2: Get the argmax of the "type" output
    type_pred = np.argmax(car_type)

    return color_pred, type_pred
```

## `app.py`

Within `app.py`, the main work is just to call `preprocess_input` and `handle_output` in
the correct locations. You can feed `args.m` into these so they receive the model type,
and will return the appropriate preprocessing or output handling function. You can then feed
the input image or output in as applicable.

```
preprocessed_image = preprocessing(image, h, w)
...
output_func = handle_output(args.t)
processed_output = output_func(output, image.shape)
```

The rest of the app will then create the relevant output images so you can see the Inference
Engine at work with the Pre-Trained Models you've worked with throughout the lesson.

Here are the commands I used to run the app for each:

```
python app.py -i "images/blue-car.jpg" -t "CAR_META" -m "/home/workspace/models/vehicle-attributes-recognition-barrier-0039.xml" -c "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"
```

```
python app.py -i "images/sign.jpg" -t "TEXT" -m "/home/workspace/models/text-detection-0004.xml" -c "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"
```

```
python app.py -i "images/sitting-on-car.jpg" -t "POSE" -m "/home/workspace/models/human-pose-estimation-0001.xml" -c "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"
```
