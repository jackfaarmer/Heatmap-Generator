# AI Heatmap Generation for On-stage Presentations
## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Using the Program](#using-the-program)
- [Contact](#contact)

## Description

This project creates a heatmap based on a subject's movement from captured video. It will highlight areas of longer duration to showcase where the subject spend the most time while "on screen".

The program is dependent on:
- Python 3.10
- OpenCV 2
- Qt for Python
- Matplotlib

In order to run this program, your machine will need the following:
- MacOS or Linux (Windows not supported at this time)
- Python 3.10 or better
- An internet connection
- A camera

If your machine is missing any of the above, please try to resolve before contacting the creator (information listed below).

## Getting Started

To get started, please run `setup.sh` in your terminal with 
```bash
bash setup.sh
```
This will check your system to see if dependencies are installed, as well as install additional dependencies within the virtual environment that is initialized to run the program.

Before using the program, make sure to activate the virtual environment by running the following commands
```bash
python3 -m venv ./venv
source venv/bin/activate
```
To use the program, please run `main.py` in your terminal with
```bash
python3 main.py
```
This will launch the program and present the user with the welcome screen.

## Using the Program

Once the user launches the program, they are brought to a welcome screen with 4 options:
- Start capture
    - Allows the user to begin video capture for heatmap calculations
    - *NOTE*: This can only be run once, afterwards the program must be restarted
- Stop capture
    - Allows the user to stop video capture and display the heatmap
- Select File
    - Will display images in the user interface
    - Intended for heatmap graphs
- Exit
    - Will exit the program

Text will be displayed in the upper-central portion of the window with the current status of the program.


## Contact

If there are any questions or concerns with this project, please direct any messages to
[john.farmer.19@cnu.edu](mailto:john.farmer.19@cnu.edu)
