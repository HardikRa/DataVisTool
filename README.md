# DataVisTool

##  Introduction

This is a python-based project which is useful in visualization of data that is very often taken as a serious headache by most people. Data is hard for a normal human to comprehend because it looks like a set of useless numbers often in the thousands or the millions, leaving most people scratching their heads about what to do with these. However, these numbers are not useless at all! In fact they are crucial to learning about any experiment or pattern. If we go to the very foundation of science, it involves catching the recurring patterns in nature, we have however come a long way from the beginning and require more apt conclusions from these patterns of numbers for them to be of any value to us.

## How to use:

Git should be preinstalled before using this tool.

Open a terminal window (or you can use one from inside VS Code), you can navigate to the file where you wish to save the files for this project and then run the command:

git clone https://github.com/HardikRa/DataVisTool.git -b master

After this, it is recommended you set up a virtual environment to run/work on the tool, Python has a tool inbuilt to do so and the process can be found easily on Google

Run the following command to install the required libraries:

pip install pandas numpy matplotlib tk

or if you have an old version of Python 2 installed on your device, run the command below:

pip3 install pandas numpy matplotlib tk

Make sure the virtual environment with the libraries installed is active, then navigate to the folder with the cloned repository and run the command:

python App.py

OR

python3 App.py

## Architecture:

What module is processing what data and giving what output

## Screenshots:


## Resources I used to build the app:
https://www.geeksforgeeks.org/python-askopenfile-function-in-tkinter/

https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/

https://www.w3schools.com/python/matplotlib_labels.asp

https://codeloop.org/how-to-embed-matplotlib-in-tkinter-window/

https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html?highlight=heatmap

https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html#sphx-glr-gallery-text-labels-and-annotations-date-py

To create ticks on date-tick chart: https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator

For using a refreshed version/custom dataset: https://www.geeksforgeeks.org/python-askopenfile-function-in-tkinter/

If you want to make one that updates live:
https://www.geeksforgeeks.org/how-to-create-a-covid19-data-representation-gui/
