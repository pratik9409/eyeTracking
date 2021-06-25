# eyeTracking

The "shape_predictor_68_face_landmarks.dat" file is in the folder trained models under gaze_tracking folder.
 
If Needed: Change your video path in "main.py" file on the line 7.

And also check inside gaze tracking folder python files are available(pupil.py, eye.py,gazetracking.py,calibration.py).

Then open the terminal and run the command "python3 main.py".

After the video starts running, a CSV file gets created in the background and is saved in the folder.

The CSV file (myrecorded_data.csv) contains the points of eyes, center and nose.

Then run the other python file for plotting the data.

"python3 raw_data.py" in the terminal.

The image of an plot will be saved in the folder where main.py file exists.
