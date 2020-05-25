# Server Communications

In this exercise, you will practice showing off your new server communication skills
for sending statistics over MQTT and images with FFMPEG.

The application itself is already built and able to perform inference, and a node server is set
up for you to use. The main node server is already fully ready to receive communications from
MQTT and FFMPEG. The MQTT node server is fully configured as well. Lastly, the ffserver is 
already configured for FFMPEG too.

The current application simply performs inference on a frame, gathers some statistics, and then 
continues onward to the next frame. 

## Tasks

Your tasks are to:

- Add any code for MQTT to the project so that the node server receives the calculated stats
  - This includes importing the relevant Python library
  - Setting IP address and port
  - Connecting to the MQTT client
  - Publishing the calculated statistics to the client
- Send the output frame (**not** the input image, but the processed output) to the ffserver

## Additional Information

Note: Since you are given the MQTT Broker Server and Node Server for the UI, you need 
certain information to correctly configure, publish and subscribe with MQTT.
- The MQTT port to use is 3001 - the classroom workspace only allows ports 3000-3009
- The topics that the UI Node Server is listening to are "class" and "speedometer"
- The Node Server will attempt to extract information from any JSON received from the MQTT server with the keys "class_names" and "speed"

## Running the App

First, get the MQTT broker and UI installed.

- `cd webservice/server`
- `npm install`
- When complete, `cd ../ui`
- And again, `npm install`

You will need *four* separate terminal windows open in order to see the results. The steps
below should be done in a different terminal based on number. You can open a new terminal
in the workspace in the upper left (File>>New>>Terminal).

1. Get the MQTT broker installed and running.
  - `cd webservice/server/node-server`
  - `node ./server.js`
  - You should see a message that `Mosca server started.`.
2. Get the UI Node Server running.
  - `cd webservice/ui`
  - `npm run dev`
  - After a few seconds, you should see `webpack: Compiled successfully.`
3. Start the ffserver
  - `sudo ffserver -f ./ffmpeg/server.conf`
4. Start the actual application. 
  - First, you need to source the environment for OpenVINO *in the new terminal*:
    - `source /opt/intel/openvino/bin/setupvars.sh -pyver 3.5`
  - To run the app, I'll give you two items to pipe in with `ffmpeg` here, with the rest up to you:
    - `-video_size 1280x720`
    - `-i - http://0.0.0.0:3004/fac.ffm`

Your app should begin running, and you should also see the MQTT broker server noting
information getting published.

In order to view the output, click on the "Open App" button below in the workspace.
