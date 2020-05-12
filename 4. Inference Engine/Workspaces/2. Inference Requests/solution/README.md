# Inference Requests - Solution

To get started, let's check out the [documentation](https://docs.openvinotoolkit.org/latest/classie__api_1_1ExecutableNetwork.html) for `ExecutableNetwork`.

I noticed two functions that seem relevant to the task at hand: `infer` and `start_async`.

While the second function pretty clearly refers to an asynchronous request based on the name, 
we can see from the notes that `infer` is used for synchronous requests. In fact, it looks like 
that function will directly return our results.

### Synchronous Request

So, if we have an `ExecutableNetwork` called `exec_net`, to make a synchronous request, 
we can do this:

```
result = exec_net.infer({'data': frame})
```

So that one is pretty quick and easy; you just need to feed the image frame in and the
synchronous request is made, returning the image.

### Asynchronous Request

The asynchronous request is a two-parter. First, you use the `start_async` function, which is
going to return a `InferRequest` object. 

```
exec_net.start_async(request_id=request_id, inputs={input_blob: frame})
```

The `input_blob` here is just the input layer of the network (`next(iter(net.inputs))`).

Since it's asynchronous, your device could be used to go ahead and capture the next frame 
of input while the current one is having inference performed on it. Therefore, to continue 
processing with the current frame, the application will need to `wait` until the current inference 
request is finished.

You can find the [documentation](https://docs.openvinotoolkit.org/latest/classie__api_1_1InferRequest.html) for `wait`
within `InferRequest`'s documentation. Back in `ExecutableNetwork`, we can see it has
a class attribute of `requests`, where you can work with the current tuple of `InferRequests`.

To use `wait`, we want to feed in a `-1` as an argument, as that will make the process wait
until the inference results are available. Otherwise, we might try to extract and handle the
model's outputs, with nothing to use.

```
status = exec_net.requests[request_id].wait(-1)
```

We can use a `request_id` of `0` here as we don't have any other requests, but if you had
another request to make, you'd use a `1` for `request_id`. 

This will return a status code - if it's `0`, the inference request is complete, and the results
can now be extracted. Let's look at that next.
