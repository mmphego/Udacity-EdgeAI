Solution: Deploy an App at the Edge
===================================

This was a tough one! It takes a little bit to step through this solution, as I want to give you some of my own techniques to approach this rather difficult problem first. The solution video is split into three parts - the first focuses on adding in the preprocessing and output handling calls within the app itself, and then into how I would approach implementing the Car Meta model's output handling.

### Early Steps and Car Meta Model Output Handling
[<img src="https://img.youtube.com/vi/X9yI7U2Rn00/maxresdefault.jpg" width="100%">](https://youtu.be/X9yI7U2Rn00)

The code for calling preprocessing and utilizing the output handling functions from within `app.py` is fairly straightforward:

```
preprocessed_image = preprocessing(image, h, w)
```

This is just feeding in the input image, along with height and width of the network, which the given `inference_network.load_model` function actually returned for you.

```
output_func = handle_output(args.t)
processed_output = output_func(output, image.shape)
```

This is partly based on the helper function I gave you, which can return the correct output handling function by feeding in the model type. The second line actually sends the output of inference and image shape to whichever output handling function is appropriate.

##### Car Meta Output Handling
[<img src="https://img.youtube.com/vi/fvFuMgYUibs/maxresdefault.jpg" width="100%">](https://youtu.be/fvFuMgYUibs)

Given that the two outputs for the Car Meta Model are `"type"` and `"color"`, and are just the softmax probabilities by class, I wanted you to just return the `np.argmax`, or the index where the highest probability was determined.

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

##### Run the Car Meta Model
[<img src="https://img.youtube.com/vi/0tuVuyD6ffM/maxresdefault.jpg" width="100%">](https://youtu.be/0tuVuyD6ffM)

I have moved the models used in the exercise into a `models` subdirectory in the `/home/workspace` directory, so the path used can be a little bit shorter.

```
python app.py -i "images/blue-car.jpg" -t "CAR_META" -m "/home/workspace/models/vehicle-attributes-recognition-barrier-0039.xml" -c "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"

```

For the other models, make sure to update the input image `-i`, model type `-t`, and model `-m` accordingly.

### Pose Estimation Output Handling

Handling the car output was fairly straightforward by using `np.argmax`, but the outputs for the pose estimation and text detection models is a bit trickier. However, there's a lot of similar code between the two. In this second part of the solution, I'll go into detail on the pose estimation model, and then we'll finish with a quick video on handling the output of the text detection model.

Pose Estimation is more difficult, and doesn't have as nicely named outputs. I noted you just need the second one in this exercise, called `'Mconv7_stage2_L2'`, which is just the keypoint heatmaps, and not the associations between these keypoints. From there, I created an empty array to hold the output heatmaps once they are re-sized, as I decided to iterate through each heatmap 1 by 1 and re-size it, which can't be done in place on the original output.

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

Note that the `input_shape[0:2][::-1]` line is taking the *original* image shape of HxWxC, taking just the first two (HxW), and reversing them to be WxH as `cv2.resize` uses.

### Text Detection Model Handling

Thanks for sticking in there! The code for the text detection model is pretty similar to the pose estimation one, so let's finish things off.

Text Detection had a very similar output processing function, just using the `'model/segm_logits/add'` output and only needing to resize over two "channels" of output. I likely could have extracted this out into its own output handling function that both Pose Estimation and Text Detection could have used.

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
