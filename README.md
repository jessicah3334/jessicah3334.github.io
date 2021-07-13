# Jessica's Personal Site

This Application was created using Python Flask (and Flask Freeze) to create a static site with my info and projects on it.

## Windows Instructions:

To get started, create a virtual environment. python -m C:\path\to\venv 

Then, activate the venv: venv\Scripts\activate.bat

Then, install dependencies: pip install -r requirements.txt

Next, export the flask app .py so flask knows what you want to run: set FLASK_APP=app.py

## Mac / Linux Instructions:

To get started, create a virtual environment. python3 -m venv venv

Then, activate the venv: venv\Scripts\activate.bat

Then, install dependencies: pip install -r requirements.txt

Next, export the flask app .py so flask knows what you want to run: export FLASK_APP=app.py

Finally, do: flask run

## Instructions for Frozen Flask: 

Once you have made desired changes to the app, run the freeze.py script to create/overwrite the flask freeze instance in the build folder. Note: this will overwrite anything you have added or has been previously written in the build folder. 

Once the build is complete, you can copy the files from inside the build folder and the entire static folder to your user.github.io and the app will automatically be deployed. 
