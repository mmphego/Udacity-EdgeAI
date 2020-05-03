# Preprocessing Inputs

Now that we have a few pre-trained models downloaded, it's time to preprocess the inputs
to match what each of the models expects as their input. We'll use the same models as before
as a basis for determining the preprocessing necessary for each input file.

As a reminder, our three models are:
- Human Pose Estimation: [human-pose-estimation-0001](https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html)
- Text Detection: [text-detection-0004](http://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html)
- Determining Car Type & Color: [vehicle-attributes-recognition-barrier-0039](https://docs.openvinotoolkit.org/latest/_models_intel_vehicle_attributes_recognition_barrier_0039_description_vehicle_attributes_recognition_barrier_0039.html)

**Note:** For ease of use, these models have been added into the `/home/workspace/models`
directory. For example, if you need to use the Text Detection model, you could find it at:

```bash
/home/workspace/models/text_detection_0004.xml
```

Each link above contains the documentation for the related model. In our case, we want to 
focus on the **Inputs** section of the page, wherein important information regarding the input
shape, order of the shape (such as color channel first or last), and the order of the color
channels, is included.

Your task is to fill out the code in three functions within `preprocess_inputs.py`, one for 
each of the three models. We have also included a potential sample image for each of the 
three models, that will be used with `test.py` to check whether the
input for each model has been adjusted as expected for proper model input.

Note that each image is **currently loaded as BGR with H, W, C order** in the `test.py` file,
so any necessary preprocessing to change that should occur in your three work files. 
Note that **BGR** order is used, as the OpenCV function we use to read images loads as
BGR, and not RGB.

When finished, you should be able to run the `test.py` file and pass all three tests.
