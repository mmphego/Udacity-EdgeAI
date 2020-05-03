# Custom Layers

This exercise is adapted from [this repository](https://github.com/david-drew/OpenVINO-Custom-Layers).

Note that the classroom workspace is running OpenVINO 2019.r3, while this exercise was
originally created for 2019.r2. This exercise will work appropriately in the workspace, but there
may be some other differences you need to account for if you use a custom layer yourself.

The below steps will walk you through the full walkthrough of creating a custom layer; as such,
there is not a related solution video. Note that custom layers is an advanced topic, and one
that is not expected to be used often (if at all) in most use cases of the OpenVINO toolkit. This
exercise is meant to introduce you to the concept, but you won't need to use it again in the 
rest of this course.

## Example Custom Layer: The Hyperbolic Cosine (cosh) Function

We will follow the steps involved for implementing a custom layer using the simple 
hyperbolic cosine (cosh) function. The cosh function is mathematically calculated as:

```
cosh(x) = (e^x + e^-x) / 2
```

As a function that calculates a value for the given value x, the cosh function is very simple 
when compared to most custom layers. Though the cosh function may not represent a "real" 
custom layer, it serves the purpose of this tutorial as an example for working through the steps 
for implementing a custom layer.

## Build the Model

First, export the below paths to shorten some of what you need to enter later:

```
export CLWS=/home/workspace/cl_tutorial
export CLT=$CLWS/OpenVINO-Custom-Layers
```

Then run the following to create the TensorFlow model including the `cosh` layer.

```
mkdir $CLWS/tf_model
python $CLT/create_tf_model/build_cosh_model.py $CLWS/tf_model
```

You should receive a message similar to:

```
Model saved in path: /tf_model/model.ckpt
```

## Creating the *`cosh`* Custom Layer

### Generate the Extension Template Files Using the Model Extension Generator

We will use the Model Extension Generator tool to automatically create templates for all the 
extensions needed by the Model Optimizer to convert and the Inference Engine to execute 
the custom layer.  The extension template files will be partially replaced by Python and C++ 
code to implement the functionality of `cosh` as needed by the different tools.  To create 
the four extensions for the `cosh` custom layer, we run the Model Extension Generator 
with the following options:

- `--mo-tf-ext` = Generate a template for a Model Optimizer TensorFlow extractor
- `--mo-op` = Generate a template for a Model Optimizer custom layer operation
- `--ie-cpu-ext` = Generate a template for an Inference Engine CPU extension
- `--ie-gpu-ext` = Generate a template for an Inference Engine GPU extension 
- `--output_dir` = set the output directory.  Here we are using `$CLWS/cl_cosh` as the target directory to store the output from the Model Extension Generator.

To create the four extension templates for the `cosh` custom layer, given we are in the `$CLWS`
directory, we run the command:

```
mkdir cl_cosh
```

```bash
python /opt/intel/openvino/deployment_tools/tools/extension_generator/extgen.py new --mo-tf-ext --mo-op --ie-cpu-ext --ie-gpu-ext --output_dir=$CLWS/cl_cosh
```

The Model Extension Generator will start in interactive mode and prompt us with questions 
about the custom layer to be generated.  Use the text between the `[]`'s to answer each 
of the Model Extension Generator questions as follows:

```
Enter layer name: 
[cosh]

Do you want to automatically parse all parameters from the model file? (y/n)
...
[n]

Enter all parameters in the following format:
...
Enter 'q' when finished:
[q]

Do you want to change any answer (y/n) ? Default 'no'
[n]

Do you want to use the layer name as the operation name? (y/n)
[y]

Does your operation change shape? (y/n)  
[n]

Do you want to change any answer (y/n) ? Default 'no'
[n]
```

When complete, the output text will appear similar to:
```
Stub file for TensorFlow Model Optimizer extractor is in /home/<user>/cl_tutorial/cl_cosh/user_mo_extensions/front/tf folder
Stub file for the Model Optimizer operation is in /home/<user>/cl_tutorial/cl_cosh/user_mo_extensions/ops folder
Stub files for the Inference Engine CPU extension are in /home/<user>/cl_tutorial/cl_cosh/user_ie_extensions/cpu folder
Stub files for the Inference Engine GPU extension are in /home/<user>/cl_tutorial/cl_cosh/user_ie_extensions/gpu folder
```

Template files (containing source code stubs) that may need to be edited have just been 
created in the following locations:

- TensorFlow Model Optimizer extractor extension: 
  - `$CLWS/cl_cosh/user_mo_extensions/front/tf/`
  - `cosh_ext.py`
- Model Optimizer operation extension:
  - `$CLWS/cl_cosh/user_mo_extensions/ops`
  - `cosh.py`
- Inference Engine CPU extension:
  - `$CLWS/cl_cosh/user_ie_extensions/cpu`
  - `ext_cosh.cpp`
  - `CMakeLists.txt`
- Inference Engine GPU extension:
  - `$CLWS/cl_cosh/user_ie_extensions/gpu`
  - `cosh_kernel.cl`
  - `cosh_kernel.xml`

Instructions on editing the template files are provided in later parts of this tutorial.  
For reference, or to copy to make the changes quicker, pre-edited template files are provided 
by the tutorial in the `$CLT` directory.

## Using Model Optimizer to Generate IR Files Containing the Custom Layer 

We will now use the generated extractor and operation extensions with the Model Optimizer 
to generate the model IR files needed by the Inference Engine.  The steps covered are:

1. Edit the extractor extension template file (already done - we will review it here)
2. Edit the operation extension template file (already done - we will review it here)
3. Generate the Model IR Files

### Edit the Extractor Extension Template File

For the `cosh` custom layer, the generated extractor extension does not need to be modified 
because the layer parameters are used without modification.  Below is a walkthrough of 
the Python code for the extractor extension that appears in the file 
`$CLWS/cl_cosh/user_mo_extensions/front/tf/cosh_ext.py`.
1. Using the text editor, open the extractor extension source file `$CLWS/cl_cosh/user_mo_extensions/front/tf/cosh_ext.py`.
2. The class is defined with the unique name `coshFrontExtractor` that inherits from the base extractor `FrontExtractorOp` class.  The class variable `op` is set to the name of the layer operation and `enabled` is set to tell the Model Optimizer to use (`True`) or exclude (`False`) the layer during processing.

    ```python
    class coshFrontExtractor(FrontExtractorOp):
        op = 'cosh' 
        enabled = True
    ```

3. The `extract` function is overridden to allow modifications while extracting parameters from layers within the input model.

    ```python
    @staticmethod
    def extract(node):
    ```

4. The layer parameters are extracted from the input model and stored in `param`.  This is where the layer parameters in `param` may be retrieved and used as needed.  For the `cosh` custom layer, the `op` attribute is simply set to the name of the operation extension used.

    ```python
    proto_layer = node.pb
    param = proto_layer.attr
    # extracting parameters from TensorFlow layer and prepare them for IR
    attrs = {
        'op': __class__.op
    }
    ```

5. The attributes for the specific node are updated. This is where we can modify or create attributes in `attrs` before updating `node` with the results and the `enabled` class variable is returned.

    ```python
    # update the attributes of the node
    Op.get_op_class_by_name(__class__.op).update_node_stat(node, attrs)
    
    return __class__.enabled
    ```

### Edit the Operation Extension Template File

For the `cosh` custom layer, the generated operation extension does not need to be modified 
because the shape (i.e., dimensions) of the layer output is the same as the input shape.  
Below is a walkthrough of the Python code for the operation extension that appears in 
the file  `$CLWS/cl_cosh/user_mo_extensions/ops/cosh.py`.

1. Using the text editor, open the operation extension source file `$CLWS/cl_cosh/user_mo_extensions/ops/cosh.py` 
2. The class is defined with the unique name `coshOp` that inherits from the base operation `Op` class.  The class variable `op` is set to `'cosh'`, the name of the layer operation.

    ```python
    class coshOp(Op):
    op = 'cosh'
    ```

3. The `coshOp` class initializer `__init__` function will be called for each layer created.  The initializer must initialize the super class `Op` by passing the `graph` and `attrs` arguments along with a dictionary of the mandatory properties for the `cosh` operation layer that define the type (`type`), operation (`op`), and inference function (`infer`).  This is where any other initialization needed by the `coshOP` operation can be specified.

    ```python
    def __init__(self, graph, attrs):
        mandatory_props = dict(
            type=__class__.op,
            op=__class__.op,
            infer=coshOp.infer            
        )
    super().__init__(graph, mandatory_props, attrs)
    ```

4. The `infer` function is defined to provide the Model Optimizer information on a layer, specifically returning the shape of the layer output for each node.  Here, the layer output shape is the same as the input and the value of the helper function `copy_shape_infer(node)` is returned.

    ```python
    @staticmethod
    def infer(node: Node):
        # ==========================================================
        # You should add your shape calculation implementation here
        # If a layer input shape is different to the output one
        # it means that it changes shape and you need to implement
        # it on your own. Otherwise, use copy_shape_infer(node).
        # ==========================================================
        return copy_shape_infer(node)
    ```

### Generate the Model IR Files

With the extensions now complete, we use the Model Optimizer to convert and optimize 
the example TensorFlow model into IR files that will run inference using the Inference Engine.  
To create the IR files, we run the Model Optimizer for TensorFlow `mo_tf.py` with 
the following options:

- `--input_meta_graph model.ckpt.meta`
  - Specifies the model input file.  

- `--batch 1`
  - Explicitly sets the batch size to 1 because the example model has an input dimension of "-1".
  - TensorFlow allows "-1" as a variable indicating "to be filled in later", however the Model Optimizer requires explicit information for the optimization process.  

- `--output "ModCosh/Activation_8/softmax_output"`
  - The full name of the final output layer of the model.

- `--extensions $CLWS/cl_cosh/user_mo_extensions`
  - Location of the extractor and operation extensions for the custom layer to be used by the Model Optimizer during model extraction and optimization. 

- `--output_dir $CLWS/cl_ext_cosh`
  - Location to write the output IR files.

To create the model IR files that will include the `cosh` custom layer, we run the commands:

```bash
cd $CLWS/tf_model
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_meta_graph model.ckpt.meta --batch 1 --output "ModCosh/Activation_8/softmax_output" --extensions $CLWS/cl_cosh/user_mo_extensions --output_dir $CLWS/cl_ext_cosh
```

The output will appear similar to:

```
[ SUCCESS ] Generated IR model.
[ SUCCESS ] XML file: /home/<user>/cl_tutorial/cl_ext_cosh/model.ckpt.xml
[ SUCCESS ] BIN file: /home/<user>/cl_tutorial/cl_ext_cosh/model.ckpt.bin
[ SUCCESS ] Total execution time: x.xx seconds.
```

## Inference Engine Custom Layer Implementation for the Intel® CPU

We will now use the generated CPU extension with the Inference Engine to execute 
the custom layer on the CPU.  The steps are:

1. Edit the CPU extension template files.
2. Compile the CPU extension library.
3. Execute the Model with the custom layer.

You *will* need to make the changes in this section to the related files.

Note that the classroom workspace only has an Intel CPU available, so we will not perform
the necessary steps for GPU usage with the Inference Engine.

### Edit the CPU Extension Template Files

The generated CPU extension includes the template file `ext_cosh.cpp` that must be edited 
to fill-in the functionality of the `cosh` custom layer for execution by the Inference Engine.  
We also need to edit the `CMakeLists.txt` file to add any header file or library dependencies 
required to compile the CPU extension.  In the next sections, we will walk through and edit 
these files.

#### Edit `ext_cosh.cpp`

We will now edit the `ext_cosh.cpp` by walking through the code and making the necessary 
changes for the `cosh` custom layer along the way.

1. Using the text editor, open the CPU extension source file `$CLWS/cl_cosh/user_ie_extensions/cpu/ext_cosh.cpp`.

2. To implement the `cosh` function to efficiently execute in parallel, the code will use the parallel processing supported by the Inference Engine through the use of the Intel® Threading Building Blocks library.  To use the library, at the top we must include the header [`ie_parallel.hpp`](https://docs.openvinotoolkit.org/2019_R3.1/ie__parallel_8hpp.html) file by adding the `#include` line as shown below.

    Before:

    ```cpp
    #include "ext_base.hpp"
    #include <cmath>
    ```

    After:

    ```cpp
    #include "ext_base.hpp"
    #include "ie_parallel.hpp"
    #include <cmath>
    ```

3. The class `coshImp` implements the `cosh` custom layer and inherits from the extension layer base class `ExtLayerBase`.

    ```cpp
    class coshImpl: public ExtLayerBase {
        public:
    ```

4. The `coshImpl` constructor is passed the `layer` object that it is associated with to provide access to any layer parameters that may be needed when implementing the specific instance of the custom layer.

    ```cpp
    explicit coshImpl(const CNNLayer* layer) {
      try {
        ...
    ```

5. The `coshImpl` constructor configures the input and output data layout for the custom layer by calling `addConfig()`.  In the template file, the line is commented-out and we will replace it to indicate that `layer` uses `DataConfigurator(ConfLayout::PLN)` (plain or linear) data for both input and output.

    Before:

    ```cpp
    ...
    // addConfig({DataConfigurator(ConfLayout::PLN), DataConfigurator(ConfLayout::PLN)}, {DataConfigurator(ConfLayout::PLN)});

    ```

    After:

    ```cpp
    addConfig(layer, { DataConfigurator(ConfLayout::PLN) }, { DataConfigurator(ConfLayout::PLN) });
    ```

6. The construct is now complete, catching and reporting certain exceptions that may have been thrown before exiting.

    ```cpp
      } catch (InferenceEngine::details::InferenceEngineException &ex) {
        errorMsg = ex.what();
      }
    }
    ```

7. The `execute` method is overridden to implement the functionality of the `cosh` custom layer.  The `inputs` and `outputs` are the data buffers passed as [`Blob`](https://docs.openvinotoolkit.org/2019_R3.1/_docs_IE_DG_Memory_primitives.html) objects.  The template file will simply return `NOT_IMPLEMENTED` by default.  To calculate the `cosh` custom layer, we will replace the `execute` method with the code needed to calculate the `cosh` function in parallel using the [`parallel_for3d`](https://docs.openvinotoolkit.org/2019_R3.1/ie__parallel_8hpp.html) function.

    Before:

    ```cpp
      StatusCode execute(std::vector<Blob::Ptr>& inputs, std::vector<Blob::Ptr>& outputs,
        ResponseDesc *resp) noexcept override {
        // Add here implementation for layer inference
        // Examples of implementations you can find in Inference Engine tool samples/extensions folder
        return NOT_IMPLEMENTED;
    ```

    After:
    ```cpp
      StatusCode execute(std::vector<Blob::Ptr>& inputs, std::vector<Blob::Ptr>& outputs,
        ResponseDesc *resp) noexcept override {
        // Add implementation for layer inference here
        // Examples of implementations are in OpenVINO samples/extensions folder

        // Get pointers to source and destination buffers
        float* src_data = inputs[0]->buffer();
        float* dst_data = outputs[0]->buffer();

        // Get the dimensions from the input (output dimensions are the same)
        SizeVector dims = inputs[0]->getTensorDesc().getDims();

        // Get dimensions:N=Batch size, C=Number of Channels, H=Height, W=Width
        int N = static_cast<int>((dims.size() > 0) ? dims[0] : 1);
        int C = static_cast<int>((dims.size() > 1) ? dims[1] : 1);
        int H = static_cast<int>((dims.size() > 2) ? dims[2] : 1);
        int W = static_cast<int>((dims.size() > 3) ? dims[3] : 1);

        // Perform (in parallel) the hyperbolic cosine given by: 
        //    cosh(x) = (e^x + e^-x)/2
        parallel_for3d(N, C, H, [&](int b, int c, int h) {
        // Fill output_sequences with -1
        for (size_t ii = 0; ii < b*c; ii++) {
          dst_data[ii] = (exp(src_data[ii]) + exp(-src_data[ii]))/2;
        }
      });
    return OK;
    }
    ```

#### Edit `CMakeLists.txt`

Because the implementation of the `cosh` custom layer makes use of the parallel processing 
supported by the Inference Engine, we need to add the Intel® Threading Building Blocks 
dependency to `CMakeLists.txt` before compiling.  We will add paths to the header 
and library files and add the Intel® Threading Building Blocks library to the list of link libraries. 
We will also rename the `.so`.

1. Using the text editor, open the CPU extension CMake file `$CLWS/cl_cosh/user_ie_extensions/cpu/CMakeLists.txt`.
2. At the top, rename the `TARGET_NAME` so that the compiled library is named `libcosh_cpu_extension.so`:

    Before:

    ```cmake
    set(TARGET_NAME "user_cpu_extension")
    ```

    After:
    
    ```cmake
    set(TARGET_NAME "cosh_cpu_extension")
    ```

3. We modify the `include_directories` to add the header include path for the Intel® Threading Building Blocks library located in `/opt/intel/openvino/deployment_tools/inference_engine/external/tbb/include`:

    Before:

    ```cmake
    include_directories (PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/common
    ${InferenceEngine_INCLUDE_DIRS}
    )
    ```

    After:
    ```cmake
    include_directories (PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/common
    ${InferenceEngine_INCLUDE_DIRS}
    "/opt/intel/openvino/deployment_tools/inference_engine/external/tbb/include"
    )
    ```

4. We add the `link_directories` with the path to the Intel® Threading Building Blocks library binaries at `/opt/intel/openvino/deployment_tools/inference_engine/external/tbb/lib`:

    Before:

    ```cmake
    ...
    #enable_omp()
    ```

    After:
    ```cmake
    ...
    link_directories(
    "/opt/intel/openvino/deployment_tools/inference_engine/external/tbb/lib"
    )
    #enable_omp()
    ```

5. Finally, we add the Intel® Threading Building Blocks library `tbb` to the list of link libraries in `target_link_libraries`:

    Before:

    ```cmake
    target_link_libraries(${TARGET_NAME} ${InferenceEngine_LIBRARIES} ${intel_omp_lib})
    ```

    After:

    ```cmake
    target_link_libraries(${TARGET_NAME} ${InferenceEngine_LIBRARIES} ${intel_omp_lib} tbb)
    ```

### Compile the Extension Library

To run the custom layer on the CPU during inference, the edited extension C++ source code 
must be compiled to create a `.so` shared library used by the Inference Engine. 
In the following steps, we will now compile the extension C++ library.

1. First, we run the following commands to use CMake to setup for compiling:

    ```bash
    cd $CLWS/cl_cosh/user_ie_extensions/cpu
    mkdir -p build
    cd build
    cmake ..
    ```

    The output will appear similar to:     

    ```
    -- Generating done
    -- Build files have been written to: /home/<user>/cl_tutorial/cl_cosh/user_ie_extensions/cpu/build
    ```

2. The CPU extension library is now ready to be compiled.  Compile the library using the command:

    ```bash
    make -j $(nproc)
    ```

    The output will appear similar to: 

    ```
    [100%] Linking CXX shared library libcosh_cpu_extension.so
    [100%] Built target cosh_cpu_extension
    ```

## Execute the Model with the Custom Layer

### Using a C++ Sample

To start on a C++ sample, we first need to build the C++ samples for use with the Inference
Engine:

```bash
cd /opt/intel/openvino/deployment_tools/inference_engine/samples/
./build_samples.sh
```

This will take a few minutes to compile all of the samples.

Next, we will try running the C++ sample without including the `cosh` extension library to see 
the error describing the unsupported `cosh` operation using the command:  

```bash
~/inference_engine_samples_build/intel64/Release/classification_sample_async -i $CLT/pics/dog.bmp -m $CLWS/cl_ext_cosh/model.ckpt.xml -d CPU
```

The error output will be similar to:

```
[ ERROR ] Unsupported primitive of type: cosh name: ModCosh/cosh/Cosh
```

We will now run the command again, this time with the `cosh` extension library specified 
using the `-l $CLWS/cl_cosh/user_ie_extensions/cpu/build/libcosh_cpu_extension.so` option 
in the command:

```bash
~/inference_engine_samples_build/intel64/Release/classification_sample_async -i $CLT/pics/dog.bmp -m $CLWS/cl_ext_cosh/model.ckpt.xml -d CPU -l $CLWS/cl_cosh/user_ie_extensions/cpu/build/libcosh_cpu_extension.so
```

The output will appear similar to:

```
Image /home/<user>/cl_tutorial/OpenVINO-Custom-Layers/pics/dog.bmp

classid probability
------- -----------
0       0.9308984  
1       0.0691015

total inference time: xx.xxxxxxx
Average running time of one iteration: xx.xxxxxxx ms

Throughput: xx.xxxxxxx FPS

[ INFO ] Execution successful
```

### Using a Python Sample

First, we will try running the Python sample without including the `cosh` extension library 
to see the error describing the unsupported `cosh` operation using the command:  

```bash
python /opt/intel/openvino/deployment_tools/inference_engine/samples/python_samples/classification_sample_async/classification_sample_async.py -i $CLT/pics/dog.bmp -m $CLWS/cl_ext_cosh/model.ckpt.xml -d CPU
```

The error output will be similar to:

```
[ INFO ] Loading network files:
/home/<user>/cl_tutorial/tf_model/model.ckpt.xml
/home/<user>/cl_tutorial/tf_model/model.ckpt.bin
[ ERROR ] Following layers are not supported by the plugin for specified device CPU:
ModCosh/cosh/Cosh, ModCosh/cosh_1/Cosh, ModCosh/cosh_2/Cosh
[ ERROR ] Please try to specify cpu extensions library path in sample's command line parameters using -l or --cpu_extension command line argument
```

We will now run the command again, this time with the `cosh` extension library specified 
using the `-l $CLWS/cl_cosh/user_ie_extensions/cpu/build/libcosh_cpu_extension.so` option 
in the command:

```bash
python /opt/intel/openvino/deployment_tools/inference_engine/samples/python_samples/classification_sample_async/classification_sample_async.py -i $CLT/pics/dog.bmp -m $CLWS/cl_ext_cosh/model.ckpt.xml -l $CLWS/cl_cosh/user_ie_extensions/cpu/build/libcosh_cpu_extension.so -d CPU
```

The output will appear similar to:

```
Image /home/<user>/cl_tutorial/OpenVINO-Custom-Layers/pics/dog.bmp

classid probability
------- -----------
0      0.9308984
1      0.0691015
```
