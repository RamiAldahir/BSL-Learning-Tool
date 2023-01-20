______________________________________________
The use of Roboflow
______________________________________________

Roboflow was used to get the labels for images in the custom dataset (collected by myself).
While roboflow also has the ability to add the neccisary folders to the program directly, it was found that this brings up a few issues with pathing.
Therefore, a new folder outside of ../yolov5 was manually made called 'data'. This folder has all of the images used as well as their labels. The
roboflow-created folders now just contain images for the test and validation images.


______________________________________________
Issues
______________________________________________

> //SOLVED\\ > There is no way to turn on the camera in Google Colab with OpenCV. This was solved by switching IDEs to Visual Studio Code - 14/11/2022

> //SOLVED\\ > The biggest issue when making this model was having the camera not turn on when cv2.VideoCapture(0) was ran.
This was fixed by uninstalling and reinstalling the cv2 library through the terminal (or Command Prompt) only.  - 20/11/2022

> //SOLVED\\ > The pre-generated roboflow data.yaml file had an incorrect layout as well as pathing, to fix this, a new file called 'sign_language_dataset.yaml' 
was manually created and called upon where needed. - 29/11/2022

> The program will only detect gestures if the user in a particular spot and under the perfect lighting conditions. This can be solved by
making more defined and varied labels per image in the training set. I will most likely have to redo the dataset for this.  - 06/12/2022

> To display the messages, buttons were used instead of labels.These are more hardware intensive. 
At the moment I cannot fit them to a label using tkinter - 18/12/2022

> When the program crashes, it displays error message saying that there is a dead kernal. 
The only way to fix this is by reopening VSC - 16/12/2022


______________________________________________
Log
______________________________________________

> The letter x never works with the current model - 01/12/2022
> Gets confused between vowls due to them having very similar gestures - 01/12/2022
> Gets confused with the letters 'l', 'n', and (rarely), 'v' - 01/12/2022
> The letter s is very hard to detect due to it having more depth than any other letter - 06/12/2022
> The model needs a very specific light level to work accuratly. The model did not work at all when testing at the campus labs - 06/12/2022
> Added simple GUI functionality with a start and stop button - 06/12/2022
> Class names are now displayed under the image and ot on the image itself as the model - 18/12/2022
