# Inference Requests

In the previous exercise, you loaded Intermediate Representations (IRs) into the Inference
Engine. Now that we've covered some of the topics around requests, including the difference
between synchronous and asynchronous requests, you'll add additional code to make
inference requests to the Inference Engine.

Given an `ExecutableNetwork` that is the IR loaded into the Inference Engine, your task is to:

1. Perform a synchronous request
2. Start an asynchronous request given an input image frame
3. Wait for the asynchronous request to complete

Note that we'll cover handling the results of the request shortly, so you don't need to worry
about that just yet. This will get you practice with both types of requests with the Inference
Engine.

You will perform the above tasks within `inference.py`. This will take three arguments,
one for the model, one for the test image, and the last for what type of inference request
should be made.

You can use `test.py` afterward to verify your code successfully makes inference requests.
