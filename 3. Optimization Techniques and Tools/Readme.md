# Optimization Techniques and Tools

# 1. Introduction to Software Optimization

# 2. Reducing Model Operations

# 3. Reducing Model Size

## Introduction to Quantization

> Broadly speaking, quantization is the process of mapping values from a larger set to a smaller one. In quantization, we might start off with a continuous (and perhaps infinite) number of possible values, and map these to a smaller (finite) set of values. In other words, quantization is the process of reducing large numbers of continuous values down into a limited number of discrete quantities.

We can use quantization to map very large numbers of high-precision weight values to a lower number of lower-precision weight values - thus reducing the size of the model by reducing the number of bits we use to store each weight.

[https://youtu.be/LVeXqd8QMMk](https://youtu.be/LVeXqd8QMMk)

## **How Quantisation is done!**

The simplest form of quantisation is **weight quantisation,** in which the amount of space required for weight values is reduced such as reducing weight values from 32bits to 8bits.

[https://youtu.be/JIz411TAM_M](https://youtu.be/JIz411TAM_M)

In order to map the weight values, we need to know:

- The range of the current set of values.
- The range of the values we are mapping to, and
- The precision of the output values.

## Further Learning

The quantization method mentioned about is one of the simplest methods to quantize a neural network, but it has some limitations. Since then, many other quantization techniques have been
proposed. For further reading checkout the paper, [A Survey on Methods and Theories of Quantized Neural Networks](https://arxiv.org/pdf/1808.04752.pdf) by Yunhui Guo, in which the author goes over some of these techniques.

OpenVINO uses MKL-DNN, a math kernel library, to quantize their
neural networks. You can find information about their quantization
workflow [here](https://intel.github.io/mkl-dnn/ex_int8_simplenet.html).

# Benchmarking Model Perfomance

**Deep Learning Workbench (DL Workbench)** is a GUI tool for OpenVINO that can be used to benchmark models and perform optimisation on them.

I needed to download and install the **DL Workbench**. Detailed instructions can be found [here](https://docs.openvinotoolkit.org/latest/_docs_Workbench_DG_Install_Workbench.html).

TD;LR

- Download `docker` (for Ubuntu 16.04 and 18.04) or `Docker Desktop` (for Windows and Mac).
- Run the `docker` command
    - For Linux and Windows you can find the docker command [here](https://docs.openvinotoolkit.org/latest/_docs_Workbench_DG_Install_from_Docker_Hub.html#install_dl_workbench_from_docker_hub_on_windows_os)
    - You can also start the DL Workbench using your OpenVINO toolkit package. Instructions for that can be found [here](https://docs.openvinotoolkit.org/latest/_docs_Workbench_DG_Install_from_Package.html)

[https://youtu.be/DkRozCswH8A](https://youtu.be/DkRozCswH8A)

In conclusion, DL Workbench can help us get accurate performance
metrics about our model. But there are a few points that you should keep in mind when interpreting the results you get:

- **DL Workbench only gives performance results of your model and not your application code.** There might be bottlenecks in your application code that could cause
your system to perform poorly. We will see how to measure these
bottlenecks in the next lesson.
- **DL Workbench gives you performance results only for the hardware you select.** You might get different results for different hardware.
- **Even though the model might give you the best performance at a certain value of batches and streams for a given hardware, your
scenario may not generate data fast enough to fulfill those batch and
stream requirements.** In a situation like this, your model will
have to wait for data, which might offset the performance gains of
batching and streaming. You should therefore select the batch and stream sizes that takes into account not only the throughput and latency, but
also how data is generated in your application

## Model Compression

*Model compression* refers to a group of algorithms that help us reduce the amount of memory needed to store a model, and also make the model more compact in terms of number of parameters.

### Weight Sharing

In *weight sharing* the goal is for multiple weights to share the same value. This reduces the number of unique weights that need to be stored thus saving memory by reducing  the size.

[https://youtu.be/qdKWq9c0o_w](https://youtu.be/qdKWq9c0o_w)

## Further Learning

Here are the articles we referenced in the video:

- [Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding (Han et al., 2016)](https://video.udacity-data.com/topher/2020/March/5e6e9c50_deep-compression-compressing-deep-neural-networks-with-pruning-trained-quantization-and-huffman-coding/deep-compression-compressing-deep-neural-networks-with-pruning-trained-quantization-and-huffman-coding.pdf)
- [Compressing Neural Networks with the Hashing Trick (Chen et al, 2015)](https://video.udacity-data.com/topher/2020/March/5e6e9c9f_compressing-neural-networks-with-the-hashing-trick/compressing-neural-networks-with-the-hashing-trick.pdf)

### Knowledge Distillation

*Knowledge distillation* is a method where we try to tranfer the knowldge learned by a large, accurate model to a smaller and computationally less expensive model.

[https://youtu.be/I--UKH27iEE](https://youtu.be/I--UKH27iEE)

## Further Learning

The generalised knowledge distillation technique we learned was introduce in a paper called **[Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)** and was written by Geoffrey Hinton, Oriol Vinyals and Jeff Dean.

Knowledge Distillation is simple, but recent works have shown that it can be a very powerful method of learning. In a recent paper,
researchers showed that by making some small changes to the knowledge
distillation algorithm, they could improve the Top-1% Accuracy on
ImageNet by 2% over the state of the art while using a model with 349M
fewer parameters! If you're curious, you can check out the full paper
here:

- [Self-training with Noisy Student improves ImageNet classification (Xie et al., 2020)](https://video.udacity-data.com/topher/2020/March/5e6ea044_self-training-with-noisy-student-improves-imagenet-classification/self-training-with-noisy-student-improves-imagenet-classification.pdf)

Note that the aim of the authors was actually *not* to compress a model, but to improve accuracy. The reduction in parameters came from using the *EfficientNet* architecture.

Knowledge distillation can also be combined with quantization as shown in **[Model compression via distillation and quantization](https://arxiv.org/abs/1802.05668)** and with pruning as shown in **[Faster gaze prediction with dense networks and Fisher pruning](https://arxiv.org/abs/1801.05787)**.

More on Knowledge distilation in deep learning: ht[tps://medium.com/analytics-vidhya/knowledge-distillation-dark-knowledge-of-neural-network-9c1dfb418e6a](https://medium.com/analytics-vidhya/knowledge-distillation-dark-knowledge-of-neural-network-9c1dfb418e6a)

---

Some cases, model inference is not actually the bottleneck - in which case, optimizing the model won't help and might even do more harm by reducing the model's accuracy.

When model inference is not the issue, we would consider profiling it for hotspots, optimising and refactoring the code.

## Introduction to Intel VTune Amplifier

---

---

---

---
