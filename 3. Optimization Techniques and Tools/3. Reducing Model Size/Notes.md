# 3. Reducing Model Size

## Introduction to Quantization
> Broadly speaking, **quantization** is the process of mapping values from a
> larger set to a smaller one. In quantization, we might start off with a
> continuous (and perhaps infinite) number of possible values, and map these
> to a smaller (finite) set of values. In other words, quantization is the
> process of reducing large numbers of continuous values down into a limited
> number of discrete quantities.

We can use quantization to map very large numbers of high-precision weight values to a lower number of lower-precision weight values—thus reducing the size of the model by reducing the number of bits we use to store each weight.
