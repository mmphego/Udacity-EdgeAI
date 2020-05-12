# Feed an IR to the Inference Engine - Solution

To start, I'll import the `IENetwork` and `IECore` from the Inference Engine. The first of
these is what will hold the Intermediate Representation object, while the second is the 
Python Plugin for working with the Inference Engine.

```
from openvino.inference_engine import IENetwork, IECore
```

I will go ahead and initialize a `plugin` variable with the `IECore` object now as well.

```
plugin = IECore()
```

Now, I can load the separate IR models into an `IENetwork` object, which I'll call `net`.

```
net = IENetwork(model=model_xml, weights=model_bin)
```

As discussed before, the `.xml` file of the IR is the model architecture, while the `.bin` file
contains weights and biases. `model_xml` and `model_bin` should be the paths to these
files.

Before loading this `net` into the `plugin`, we need to check whether all of the layers are
supported by the `plugin`. We can get the plugin's supported layers of the IR by using the
`.query_network()` function of an [`IECore`](https://docs.openvinotoolkit.org/latest/classie__api_1_1IECore.html):

```
supported_layers = plugin.query_network(network=net, device_name="CPU")
```

Note that the `device` argument here can also be `"GPU"`, `"FPGA"` or `"MYRIAD"`, depending
on what hardware is being used. `"MYRIAD"` is used for the Intel Neural Compute Stick.

Then, we can iterate through the layers in the `net` itself, to gather any unsupported layers.

```
unsupported_layers = [l for l in net.layers.keys() if l not in supported_layers]
```

If the length of the `unsupported_layers` list is not zero, the model is not going to be able
to run on this device with the Inference Engine. So, we should add a `print` statement 
or `log` to the console that an extension may be necessary, and then exit the program.

In our case, we will be able to run the included IRs by adding a CPU extension. For Linux
machines, like the classroom workspace, these are usually found in the following directory:
```
<OpenVINO install dir>/deployment_tools/inference_engine/lib/intel64
```

I hard-coded the location of the relevant CPU extension into the starter code. In this case,
it is the `libcpu_extension_sse4.so` CPU extension that you'll want to add.

Back in the `IECore` [documentation](https://docs.openvinotoolkit.org/latest/classie__api_1_1IECore.html),
we see there is an `.add_extension` function, which just takes the path to the CPU
extension and device name:

```
plugin.add_extension(cpu_extension, “CPU”)
```

Now, if we check for unsupported layers again, there should be zero that are unsupported.

Finally, we can  `.load_network` function from `IECore` to load the model into the Inference Engine:

```
plugin.load_network(net, “CPU”)
```

To make sure your implementation works appropriately, you should use each of the three
models in the workspace with `feed_network.py`, such as:

```bash
python feed_network.py -m /home/workspace/models/human-pose-estimation-0001.xml
```

Now, we're ready to start making inference requests, which we'll look at next.
