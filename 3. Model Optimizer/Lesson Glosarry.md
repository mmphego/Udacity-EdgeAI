# Lesson Glossary

#### Model Optimizer

A command-line tool used for converting a model from one of the supported frameworks to an Intermediate Representation (IR), including certain performance optimizations, that is compatible with the Inference Engine.

#### Optimization Techniques

Optimization techniques adjust the original trained model in order to either reduce the size of or increase the speed of a model in performing inference. Techniques discussed in the lesson include quantization, freezing and fusion.

#### Quantization

Reduces precision of weights and biases (to lower precision floating point values or integers), thereby reducing compute time and size with some (often minimal) loss of accuracy.

#### Freezing

In TensorFlow this removes metadata only needed for training, as well as converting variables to constants. Also a term in training neural networks, where it often refers to freezing layers themselves in order to fine tune only a subset of layers.

#### Fusion

The process of combining certain operations together into one operation and thereby needing less computational overhead. For example, a batch normalization layer, activation layer, and convolutional layer could be combined into a single operation. This can be particularly useful for GPU inference, where the separate operations may occur on separate GPU kernels, while a fused operation occurs on one kernel, thereby incurring less overhead in switching from one kernel to the next.

#### Supported Frameworks

The Intel® Distribution of OpenVINO™ Toolkit currently supports models from five frameworks (which themselves may support additional model frameworks): Caffe, TensorFlow, MXNet, ONNX, and Kaldi.

#### [Caffe](https://caffe.berkeleyvision.org/)

The "Convolutional Architecture for Fast Feature Embedding" (CAFFE) framework is an open-source deep learning library originally built at UC Berkeley.

#### [TensorFlow](https://www.tensorflow.org/)

TensorFlow is an open-source deep learning library originally built at Google. As an Easter egg for anyone who has read this far into the glossary, this was also your instructor's first deep learning framework they learned, back in 2016 (pre-V1!).

#### [MXNet](https://mxnet.apache.org/)

Apache MXNet is an open-source deep learning library built by Apache Software Foundation.

#### [ONNX](https://onnx.ai/)

The "Open Neural Network Exchange" (ONNX) framework is an open-source deep learning library originally built by Facebook and Microsoft. PyTorch and Apple-ML models are able to be converted to ONNX models.

#### [Kaldi](https://kaldi-asr.org/doc/dnn.html)

While still open-source like the other supported frameworks, Kaldi is mostly focused around speech recognition data, with the others being more generalized frameworks.

#### Intermediate Representation

A set of files converted from one of the supported frameworks, or available as one of the Pre-Trained Models. This has been optimized for inference through the Inference Engine, and may be at one of several different precision levels. Made of two files:

-   `.xml` - Describes the network topology
-   `.bin` - Contains the weights and biases in a binary file

#### Supported Layers

Layers [supported](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_Supported_Frameworks_Layers.html) for direct conversion from supported framework layers to intermediate representation layers through the Model Optimizer. While nearly every layer you will ever use is in the supported frameworks is supported, there is sometimes a need for handling Custom Layers.

#### Custom Layers

Custom layers are those outside of the list of known, supported layers, and are typically a rare exception. Handling custom layers in a neural network for use with the Model Optimizer depends somewhat on the framework used; other than adding the custom layer as an extension, you otherwise have to follow [instructions](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_customize_model_optimizer_Customize_Model_Optimizer.html) specific to the framework.
