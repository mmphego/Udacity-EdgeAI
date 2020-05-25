# Lesson Glossary


#### Edge Application

Applications with inference run on local hardware, sometimes without network connections, such as Internet of Things (IoT) devices, as opposed to the cloud. Less data needs to be streamed over a network connection, and real-time decisions can be made.

#### OpenVINO™ Toolkit

The [Intel® Distribution of OpenVINO™ Toolkit](https://software.intel.com/en-us/openvino-toolkit) enables deep learning inference at the edge by including both neural network optimizations for inference as well as hardware-based optimizations for Intel® hardware.

#### Pre-Trained Model

Computer Vision and/or AI models that are already trained on large datasets and available for use in your own applications. These models are often trained on datasets like [ImageNet](https://en.wikipedia.org/wiki/ImageNet). Pre-trained models can either be used as is or used in transfer learning to further fine-tune a model. The OpenVINO™ Toolkit provides a number of [pre-trained models](https://software.intel.com/en-us/openvino-toolkit/documentation/pretrained-models) that are already optimized for inference.

#### Transfer Learning

The use of a pre-trained model as a basis for further training of a neural network. Using a pre-trained model can help speed up training as the early layers of the network have feature extractors that work in a wide variety of applications, and often only late layers will need further fine-tuning for your own dataset. OpenVINO™ does not deal with transfer learning, as all training should occur prior to using the Model Optimizer.

#### Image Classification

A form of inference in which an object in an image is determined to be of a particular class, such as a cat vs. a dog.

#### Object Detection

A form of inference in which objects within an image are detected, and a bounding box is output based on where in the image the object was detected. Usually, this is combined with some form of classification to also output which class the detected object belongs to.

#### Semantic Segmentation

A form of inference in which objects within an image are detected and classified on a pixel-by-pixel basis, with all objects of a given class given the same label.

#### Instance Segmentation

Similar to semantic segmentation, this form of inference is done on a pixel-by-pixel basis, but different objects of the same class are separately identified.

#### [SSD](https://arxiv.org/abs/1512.02325)

A neural network combining object detection and classification, with different feature extraction layers directly feeding to the detection layer, using default bounding box sizes and shapes/

#### [YOLO](https://arxiv.org/abs/1506.02640)

One of the original neural networks to only take a single look at an input image, whereas earlier networks ran a classifier multiple times across a single image at different locations and scales.

#### [Faster R-CNN](https://arxiv.org/abs/1506.01497)

A network, expanding on [R-CNN](https://arxiv.org/pdf/1311.2524.pdf) and [Fast R-CNN](https://arxiv.org/pdf/1504.08083.pdf), that integrates advances made in the earlier models by adding a Region Proposal Network on top of the Fast R-CNN model for an integrated object detection model.

#### [MobileNet](https://arxiv.org/abs/1704.04861)

A neural network architecture optimized for speed and size with minimal loss of inference accuracy through the use of techniques like [1x1 convolutions](https://stats.stackexchange.com/questions/194142/what-does-1x1-convolution-mean-in-a-neural-network). As such, MobileNet is more useful in mobile applications that substantially larger and slower networks.

#### [ResNet](https://arxiv.org/abs/1512.03385)

A very deep neural network that made use of residual, or "skip" layers that pass information forward by a couple of layers. This helped deal with the [vanishing gradient problem](https://towardsdatascience.com/the-vanishing-gradient-problem-69bf08b15484) experienced by deeper neural networks.

#### [Inception](https://arxiv.org/pdf/1409.4842.pdf)

A neural network making use of multiple different convolutions at each "layer" of the network, such as 1x1, 3x3 and 5x5 convolutions. The top architecture from the original paper is also known as GoogLeNet, an homage to [LeNet](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf), an early neural network used for character recognition.

#### Inference Precision

Precision refers to the level of detail to weights and biases in a neural network, whether in floating point precision or integer precision. Lower precision leads to lower accuracy, but with a positive trade-off for network speed and size.
