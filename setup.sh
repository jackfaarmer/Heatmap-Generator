#!/bin/bash

echo
echo "-= AI Heatmap Generation for On-Stage Presentations =-"
echo "-=============+        SETUP        +================-"
echo

## check if python is installed on system
echo " -- Checking Python installation......."
{
    [[ "$(python3 -V)" =~ "Python 3" ]] && echo "-- Python 3 is installed"
} || {
    echo "Python 3 is NOT installed. Please install python before continuing."
    exit
}

## initialize virtual environment
python3 -m venv ./venv
source venv/bin/activate

###### if installed, move on to additional dependencies
###### if not, install

echo
echo "Checking pip installation"
echo
python3 -m ensurepip --upgrade
pip install --upgrade pip
echo "pip successfully / already installed"
echo "Installing OpenCV dependencies"

## check for OpenCV (python) and Qt (python), install if necesary

echo
pip install opencv-python

echo
pip install pyside6

echo
pip install matplotlib

echo
echo "-====== AI Heatmap generation setup COMPLETE =======-"
echo
