# The OpenVINO™ Toolkit

[<img src="https://img.youtube.com/vi/-pM9pLCnzJk/maxresdefault.jpg" width="100%">](https://youtu.be/-pM9pLCnzJk)

## The Intel® Distribution of OpenVINO™ Toolkit
The OpenVINO™ Toolkit’s name comes from “Open Visual Inferencing and Neural Network Optimization”. It is largely focused around optimizing neural network inference, and is open source.

It is developed by Intel®, and helps support fast inference across Intel® CPUs, GPUs, FPGAs and Neural Compute Stick with a common API. OpenVINO™ can take models built with multiple different frameworks, like TensorFlow or Caffe, and use its Model Optimizer to optimize for inference. This optimized model can then be used with the Inference Engine, which helps speed inference on the related hardware. It also has a wide variety of Pre-Trained Models already put through Model Optimizer.

By optimizing for model speed and size, OpenVINO™ enables running at the edge. This does not mean an increase in inference accuracy - this needs to be done in training beforehand. The smaller, quicker models OpenVINO™ generates, along with the hardware optimizations it provides, are great for lower resource applications. For example, an IoT device does not have the benefit of multiple GPUs and unlimited memory space to run its apps.

# Pre-Trained Models in OpenVINO™
[<img src="https://img.youtube.com/vi/1-Vije0cMBQ/maxresdefault.jpg" width="100%">](https://youtu.be/1-Vije0cMBQ)

In general, pre-trained models refer to models where training has already occurred, and often have high, or even cutting-edge accuracy. Using pre-trained models avoids the need for large-scale data collection and long, costly training. Given knowledge of how to preprocess the inputs and handle the outputs of the network, you can plug these directly into your own app.

In OpenVINO™, Pre-Trained Models refer specifically to the Model Zoo, in which the Free Model Set contains pre-trained models already converted using the Model Optimizer. These models can be used directly with the Inference Engine.
Further Research

We’ll come back to the various pre-trained models available with the OpenVINO™ Toolkit shortly, but you can get a headstart by checking out the documentation [here](https://software.intel.com/en-us/openvino-toolkit/documentation/pretrained-models).

# Types of Computer Vision Models
[<img src="https://img.youtube.com/vi/E8yBgSKfCoo/maxresdefault.jpg" width="100%">](https://youtu.be/E8yBgSKfCoo)

We covered three types of computer vision models in the video:
- **Classification** determines a given “class” that an image, or an object in an image, belongs to, from a simple yes/no to thousands of classes. These usually have some sort of “probability” by class, so that the highest probability is the determined class, but you can also see the top 5 predictions as well.
- **Detection** gets into determining that objects appear at different places in an image, and oftentimes draws bounding boxes around the detected objects. It also usually has some form of classification that determines the class of an object in a given bounding box. The bounding boxes have a confidence threshold so you can throw out low-confidence detections.
- **Segmentation** classifies sections of an image by classifying each and every pixel. These networks are often post-processed in some way to avoid phantom classes here and there. Within segmentation are the subsets of semantic segmentation and instance segmentation - the first wherein all instances of a class are considered as one, while the second actually consider separates instances of a class as separate objects.

Here is a useful [Medium post](https://medium.com/analytics-vidhya/image-classification-vs-object-detection-vs-image-segmentation-f36db85fe81) if you want to go a little further on types of computer vision models.

# Case Studies in Computer Vision

[<img src="https://img.youtube.com/vi/7mUaovlA4aQ/maxresdefault.jpg" width="100%">](https://youtu.be/7mUaovlA4aQ)
We focused on SSD, ResNet and MobileNet in the video. SSD is an object detection network that combined classification with object detection through the use of default bounding boxes at different network levels. ResNet utilized residual layers to “skip” over sections of layers, helping to avoid the vanishing gradient problem with very deep neural networks. MobileNet utilized layers like 1x1 convolutions to help cut down on computational complexity and network size, leading to fast inference without substantial decrease in accuracy.

One additional note here on the ResNet architecture - the paper itself actually theorizes that very deep neural networks have convergence issues due to exponentially lower convergence rates, as opposed to just the vanishing gradient problem. The vanishing gradient problem is also thought to be helped by the use of normalization of inputs to each different layer, which is not specific to ResNet. The ResNet architecture itself, at multiple different numbers of layers, was shown to converge faster during training than a “plain” network without the residual layers.

## Further Research

Getting used to reading research papers is a key skill to build when working with AI and Computer Vision. Below, you can find the original research papers on some of the networks we discussed in this section.

-   [SSD](https://arxiv.org/abs/1512.02325)
-   [YOLO](https://arxiv.org/abs/1506.02640)
-   [Faster RCNN](https://arxiv.org/abs/1506.01497)
-   [MobileNet](https://arxiv.org/abs/1704.04861)
-   [ResNet](https://arxiv.org/abs/1512.03385)
-   [Inception](https://arxiv.org/pdf/1409.4842.pdf)

# Available Pre-Trained Models in OpenVINO™

[<img src="https://img.youtube.com/vi/SoTH1jr3-HA/maxresdefault.jpg" width="100%">](https://youtu.be/SoTH1jr3-HA)
Most of the Pre-Trained Models supplied by OpenVINO™ fall into either face detection, human detection, or vehicle-related detection. There is also a model around detecting text, and more!

Models in the Public Model Set must still be run through the Model Optimizer, but have their original models available for further training and fine-tuning. The Free Model Set are already converted to Intermediate Representation format, and do not have the original model available. These can be easily obtained with the Model Downloader tool provided in the files installed with OpenVINO™.

The SSD and MobileNet architectures we discussed previously are often the main part of the architecture used for many of these models.

# Optimizations on the Pre-Trained Models

[<img src="https://img.youtube.com/vi/nKvZYnOnWm4/maxresdefault.jpg" width="100%">](https://youtu.be/nKvZYnOnWm4)
In the exercise, you dealt with different precisions of the different models. Precisions are related to floating point values - less precision means less memory used by the model, and less compute resources. However, there are some trade-offs with accuracy when using lower precision. There is also fusion, where multiple layers can be fused into a single operation. These are achieved through the Model Optimizer in OpenVINO™, although the Pre-Trained Models have already been run through that process. We’ll return to these optimization techniques in the next lesson.

# Choosing the Right Model for Your App
[<img src="https://img.youtube.com/vi/CWC195DzgAI/maxresdefault.jpg" width="100%">](https://youtu.be/CWC195DzgAI)
Make sure to test out different models for your application, comparing and contrasting their use cases and performance for your desired task. Remember that a little bit of extra processing may yield even better results, but needs to be implemented efficiently.

This goes both ways - you should try out different models for a single use case, but you should also consider how a given model can be applied to multiple use cases. For example, being able to track human poses could help in physical therapy applications to assess and track progress of limb movement range over the course of treatment.

# Pre-processing Inputs
[<img src="https://img.youtube.com/vi/E9huKos96Uk/maxresdefault.jpg" width="100%">](https://youtu.be/E9huKos96Uk)

The pre-processing needed for a network will vary, but usually this is something you can check out in any related documentation, including in the OpenVINO™ Toolkit documentation. It can even matter what library you use to load an image or frame - OpenCV, which we'll use to read and handle images in this course, reads them in the BGR format, which may not match the RGB images some networks may have used to train with.

Outside of channel order, you also need to consider image size, and the order of the image data, such as whether the color channels come first or last in the dimensions. Certain models may require a certain normalization of the images for input, such as pixel values between 0 and 1, although some networks also do this as their first layer.

In OpenCV, you can use `cv2.imread` to read in images in BGR format, and `cv2.resize` to resize them. The images will be similar to a numpy array, so you can also use array functions like `.transpose` and `.reshape` on them as well, which are useful for switching the array dimension order.

# Solution: Pre-processing Inputs

[<img src="https://img.youtube.com/vi/erNsB5nXgW4/maxresdefault.jpg" width="100%">](https://youtu.be/erNsB5nXgW4)

Using the documentation pages for each model, I ended up noticing they needed essentially the same preprocessing, outside of the height and width of the input to the network. The images coming from `cv2.imread` were already going to be BGR, and all the models wanted BGR inputs, so I didn't need to do anything there. However, each image was coming in as height x width x channels, and each of these networks wanted channels first, along with an extra dimension at the start for batch size.

So, for each network, the preprocessing needed to 1) re-size the image, 2) move the channels from last to first, and 3) add an extra dimension of `1` to the start. Here is the function I created for this, which I could call for each separate network:

```python
def preprocessing(input_image, height, width):
    '''
    Given an input image, height and width:
    - Resize to height and width
    - Transpose the final "channel" dimension to be first
    - Reshape the image to add a "batch" of 1 at the start
    '''
    image = cv2.resize(input_image, (width, height))
    image = image.transpose((2,0,1))
    image = image.reshape(1, 3, height, width)

    return image

```

Then, for each model, I can just call this function with the height and width from the documentation:

**Human Pose**

```python
preprocessed_image = preprocessing(preprocessed_image, 256, 456)
```

**Text Detection**

```python
preprocessed_image = preprocessing(preprocessed_image, 768, 1280)

```

**Car Meta**

```python
preprocessed_image = preprocessing(preprocessed_image, 72, 72)

```

# Handling Network Outputs

[<img src="https://img.youtube.com/vi/pREe4P5yygM/maxresdefault.jpg" width="100%">](https://youtu.be/pREe4P5yygM)

Like the computer vision model types we discussed earlier, we covered the primary outputs those networks create: classes, bounding boxes, and semantic labels.

Classification networks typically output an array with the softmax probabilities by class; the `argmax` of those probabilities can be matched up to an array by class for the prediction.

Bounding boxes typically come out with multiple bounding box detections per image, which each box first having a class and confidence. Low confidence detections can be ignored. From there, there are also an additional four values, two of which are an X, Y pair, while the other may be the opposite corner pair of the bounding box, or otherwise a height and width.

Semantic labels give the class for each pixel. Sometimes, these are flattened in the output, or a different size than the original image, and need to be reshaped or resized to map directly back to the input.

**Quiz Information**

In a network like [SSD](https://arxiv.org/pdf/1512.02325.pdf) that we discussed earlier, the output is a series of bounding boxes for potential object detections, typically also including a confidence threshold, or how confident the model is about that particular detection.

Therefore, inference performed on a given image will output an array with multiple bounding box predictions including: the class of the object, the confidence, and two corners (made of `xmin`, `ymin`, `xmax`, and `ymax`) that make up the bounding box, in that order.

**Further Research**

-   [Here](https://towardsdatascience.com/understanding-ssd-multibox-real-time-object-detection-in-deep-learning-495ef744fab) is a great write-up on working with SSD and its output
-   This [post](https://thegradient.pub/semantic-segmentation/) gets into more of the differences in moving from models with bounding boxes to those using semantic segmentation

# Running Your First Edge App
[<img src="https://img.youtube.com/vi/FANZZXUqGac/maxresdefault.jpg" width="100%">](https://youtu.be/FANZZXUqGac)

You have now learned the key parts of working with a pre-trained model: obtaining the model, preprocessing inputs for it, and handling its output. In the upcoming exercise, you’ll load a pre-trained model into the Inference Engine, as well as call for functions to preprocess and handle the output in the appropriate locations, from within an edge app. We’ll still be abstracting away some of the steps of dealing with the Inference Engine API until a later lesson, but these should work similarly across different models.

# Solution: Deploy an App at the Edge
See: [Solution notes](Workspaces/3.%20Deploy%20An%20App%20at%20the%20Edge/Solution.md)


