# Processing Model Outputs - Solution

My approach in this exercise was to check if the bad combination of pets was on screen,
but also to track whether I already warned them in the current incident. Now, I might also
consider re-playing the warning after a certain time period in a single consecutive incident,
but the provided video file does not really have that long of consecutive timespans.

I also output a "timestamp" by checking how many frames had been processed so far 
at 30 fps.

The next step of this, which we'll look at shortly, is how you could actually send this 
information over the Internet, so that you could get an alert or even stream the video,
if necessary.

As we get further into the lesson and consider the costs of streaming images and/or video
to a server, another consideration here could be that you also save down the video *only*
when you run into this problem situation. You could potentially have a running 30 second loop
as well stored on the local device that is constantly refreshed, but the leading 30 seconds is
stored anytime the problematic pet combination is detected.

To run the app, I just used:

```
python app.py -m model.xml
```

Since the model was provided here in the same directory.
