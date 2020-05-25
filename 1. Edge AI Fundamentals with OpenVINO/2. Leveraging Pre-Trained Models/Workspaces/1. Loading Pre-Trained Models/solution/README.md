# Loading Pre-Trained Models - Solution

In this exercise, you downloaded and loaded a few of the pre-trained models available 
in the OpenVINO toolkit.

- There's certainly some wiggle room on which pre-trained models to use for each, but I just used the primary model linked to from the [Pre-Trained Model list](https://software.intel.com/en-us/openvino-toolkit/documentation/pretrained-models) for each:
  - Human Pose Estimation: [human-pose-estimation-0001](https://docs.openvinotoolkit.org/latest/_models_intel_human_pose_estimation_0001_description_human_pose_estimation_0001.html)
  - Text Detection: [text-detection-0004](http://docs.openvinotoolkit.org/latest/_models_intel_text_detection_0004_description_text_detection_0004.html)
  - Determining Car Type & Color: [vehicle-attributes-recognition-barrier-0039](https://docs.openvinotoolkit.org/latest/_models_intel_vehicle_attributes_recognition_barrier_0039_description_vehicle_attributes_recognition_barrier_0039.html)
- To access the Model Downloader, you can `cd /opt/intel/openvino/deployment_tools/tools/model_downloader`
- From there, if you use `sudo ./downloader.py -h`, you can see the various arguments you can feed to the downloader. I noted `--name` and `--precisions`  as useful arguments to feed both the model name and which precision(s) I wanted to download.
- The format therefore is:
  - `sudo ./downloader.py --name {model-name} {--precisions {precision-levels}}`, e.g. `sudo ./downloader.py --name human-pose-estimation-0001` for all precision levels, or `sudo ./downloader.py --name text-detection-0004 --precisions FP16` for just FP16 precision, for example.
  - In the workspace, you should add a `-o` argument at the end, e.g.  `sudo ./downloader.py --name human-pose-estimation-0001 -o /home/workspace`
- I can then check the `/home/workspace/intel` directory and see that each model is in that directory, with the desired precisions included, and `.bin` and `.xml` files for each model precision. Note on a local machine this defaults to `/opt/intel/openvino/deployment_tools/open_model_zoo/tools/downloader/intel`
- Some of these directory paths are pretty long - you may want to consider adding symbolic links to these directories for faster use.
