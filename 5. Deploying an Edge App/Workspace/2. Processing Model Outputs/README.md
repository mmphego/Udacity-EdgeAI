# Processing Model Outputs

Let's say you have a cat and two dogs at your house. 

If both dogs are in a room together, they are best buds, and everything is going well.

If the cat and dog #1 are in a room together, they are also good friends, and everything is fine.

However, if the cat and dog #2 are in a room together, they don't get along, and you may need to either pull them apart, or at least play a pre-recorded message from your smart speaker to tell them to cut it out.

In this exercise, you'll receive a video where some combination or the cat and dogs may be in view. You also will have an IR that is able to determine which of these, if any, are on screen.

While the best model for this is likely an object detection model that can identify different breeds, I have provided you with a very basic (and overfit) model that will return three classes, one for one or less pets on screen, one for the bad combination of the cat and dog #2, and one for the fine combination of the cat and dog #1. This is within the exercise directory - `model.xml`.

It is up to you to add code that will print to the terminal anytime the bad combination of the cat and dog #2 are detected together. 
**Note**: It's important to consider whether you really want to output a warning *every single time* both pets are on-screen - is your warning helpful
if it re-starts every 30th of a second, with a video at 30 fps?

