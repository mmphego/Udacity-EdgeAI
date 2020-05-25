# Server Communications - Solution

Let's focus on MQTT first, and then FFmpeg.

### MQTT

First, I import the MQTT Python library. I use an alias here so the library is easier to work with.

```
import paho.mqtt.client as mqtt
```

I also need to `import socket` so I can connect to the MQTT server. Then, I can get the 
IP address and set the port for communicating with the MQTT server.

```
HOSTNAME = socket.gethostname()
IPADDRESS = socket.gethostbyname(HOSTNAME)
MQTT_HOST = IPADDRESS
MQTT_PORT = 3001
MQTT_KEEPALIVE_INTERVAL = 60
```

This will set the IP address and port, as well as the keep alive interval. The keep alive interval
is used so that the server and client will communicate every 60 seconds to confirm their
connection is still open, if no other communication (such as the inference statistics) is received.

Connecting to the client can be accomplished with:

```
client = mqtt.Client()
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
```

Note that `mqtt` in the above was my import alias - if you used something different, that line
will also differ slightly, although will still use `Client()`.

The final piece for MQTT is to actually publish the statistics to the connected client.

```
topic = "some_string"
client.publish(topic, json.dumps({"stat_name": statistic}))
```

The topic here should match to the relevant topic that is being subscribed to from the other
end, while the JSON being published should include the relevant name of the statistic for
the node server to parse (with the name like the key of a dictionary), with the statistic passed
in with it (like the items of a dictionary).

```
client.publish("class", json.dumps({"class_names": class_names}))
client.publish("speedometer", json.dumps({"speed": speed}))
```

And, at the end of processing the input stream, make sure to disconnect.

```
client.disconnect()
```

### FFmpeg

FFmpeg does not actually have any real specific imports, although we do want the standard
`sys` library

```
import sys
```

This is used as the `ffserver` can be configured to read from `sys.stdout`. Once the output
frame has been processed (drawing bounding boxes, semantic masks, etc.), you can write
the frame to the `stdout` buffer and `flush` it.

```
sys.stdout.buffer.write(frame)  
sys.stdout.flush()
```

And that's it! As long as the MQTT and FFmpeg servers are running and configured
appropriately, the information should be able to be received by the final node server, 
and viewed in the browser.

To run the app itself, with the UI server, MQTT server, and FFmpeg server also running, do:

```
python app.py | ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 1280x720 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
```

This will feed the output of the app to FFmpeg.
