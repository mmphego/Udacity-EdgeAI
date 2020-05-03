# Loading Pre-Trained Models

In this exercise, you'll work to download and load a few of the pre-trained models available 
in the OpenVINO toolkit.

First, you can navigate to the [Pre-Trained Models list](https://software.intel.com/en-us/openvino-toolkit/documentation/pretrained-models) in a separate window or tab, as well as the page that gives all of the model names [here](https://docs.openvinotoolkit.org/latest/_models_intel_index.html).

Your task here is to download the below three pre-trained models using the Model Downloader tool, as detailed on the same page as the different model names. Note that you *do not need to download all of the available pre-trained models* - doing so would cause your workspace to crash, as the workspace will limit you to 3 GB of downloaded models.

### Task 1 - Find the Right Models
Using the [Pre-Trained Model list](https://software.intel.com/en-us/openvino-toolkit/documentation/pretrained-models), determine which models could accomplish the following tasks (there may be some room here in determining which model to download):
- Human Pose Estimation
- Text Detection
- Determining Car Type & Color

### Task 2 - Download the Models
Once you have determined which model best relates to the above tasks, use the Model Downloader tool to download them into the workspace for the following precision levels:
- Human Pose Estimation: All precision levels
- Text Detection: FP16 only
- Determining Car Type & Color: INT8 only

**Note**: When downloading the models in the workspace, add the `-o` argument (along with any other necessary arguments) with `/home/workspace` as the output directory. The default download directory will not allow the files to be written there within the workspace, as it is a read-only directory.

### Task 3 - Verify the Downloads
You can verify the download of these models by navigating to: `/home/workspace/intel` (if you followed the above note), and checking whether a directory was created for each of the three models, with included subdirectories for each precision, with respective `.bin` and `.xml` for each model.

**Hint**: Use the `-h` command with the Model Downloader tool if you need to check out the possible arguments to include when downloading specific models and precisions.
