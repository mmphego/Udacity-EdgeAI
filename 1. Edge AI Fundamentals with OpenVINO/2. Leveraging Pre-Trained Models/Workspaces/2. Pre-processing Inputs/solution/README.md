# Preprocessing Inputs - Solution

### Pose Estimation

Let's start with `pose_estimation`, and it's [related documentation](https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html).

I see it is in [B, C, H, W] format, with a shape of 1x3x256x456, and an expected color order
of BGR.

Since we're loading the image with OpenCV, I know it's already in BGR format. From there, 
I need to resize the image to the desired shape, but that's going to get me 256x256x3.

```
preprocessed_image = cv2.resize(preprocessed_image, (256, 456))
```

So, I need to transpose the image, where the 3rd dimension, containing the channels,
is placed first, with the other two following.

```
preprocessed_image = preprocessed_image.transpose((2,0,1))
```

Lastly, I still need to add the `1` for the batch size at the start. I can actually just reshape
to "add" the extra dimension.

```
preprocessed_image = preprocessed_image.reshape(1,3,256,456)
```

### Text Detection

Next, let's look at `text_detection`, and it's [related documentation](http://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html).

This will actually be a very similar process to above! As such, you might actually consider
whether you could add a standard "helper" for each of these, where you could just add the
desired input shape, and perform the same transformations. Note that it does require knowing
for sure that all the steps (being in BGR, resizing, transposing, reshaping) are needed for each.

Here, the only change needed is for resizing (as well as the dimensions fed into reshape):

```
cv2.resize(preprocessed_image, (768, 1280))
```

### Car Metadata

Lastly, let's cover `car_meta`, and it's [related documentation](https://docs.openvinotoolkit.org/latest/_models_intel_vehicle_attributes_recognition_barrier_0039_description_vehicle_attributes_recognition_barrier_0039.html).

Again, all we need to change is how the image is resized, and making sure we `reshape` 
correctly:

```
cv2.resize(preprocessed_image, (72, 72))
```
