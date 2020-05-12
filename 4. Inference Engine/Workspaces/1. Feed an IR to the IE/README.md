# Feed an IR to the Inference Engine

Earlier in the course, you were focused on working with the Intermediate Representation (IR)
models themselves, while mostly glossing over the use of the actual Inference Engine with
the model.

Here, you'll import the Python wrapper for the Inference Engine (IE), and practice using 
different IRs with it. You will first add each IR as an `IENetwork`, and check whether the layers 
of that network are supported by the classroom CPU.

Since the classroom workspace is using an Intel CPU, you will also need to add a CPU
extension to the `IECore`.

Once you have verified all layers are supported (when the CPU extension is added),
you will load the given model into the Inference Engine.

Note that the `.xml` file of the IR should be given as an argument when running the script.

To test your implementation, you should be able to successfully load each of the three IR
model files we have been working with throughout the course so far, which you can find in the
`/home/workspace/models` directory.
