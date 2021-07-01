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

### Entry Page

!(<1.png>)

## Architecture:

The GUI library used for this tool is Tkinter. A multi-page Application in Tkinter is used to make the tool. The entire working of the GUI is found strictly in App.py

A custom CSV file can be used to visualize data, this is done with the help of pandas.

#### Date-Tick Graph

The date-tick graph in this case is optimized well for the Covid-19 dataset uploaded by Our World in Data, a CSV file of the same can be found in the repository, however if you would like to use a new dataset the ones found here will work perfectly with it : https://github.com/owid/covid-19-data/tree/master/public/data

The numpy library is used to convert the date into the appropriate data type before using in the graph.

Matplotlib allows addition of major and minor ticks, in this case I have used a major tick every month and minor ticks every Monday.

A Tkinter canvas is used to draw the graph within the tool.



This is after going to the date-tick page and clicking on the choose file, I used the Covid dataset to optimize it and it works quite well with that.



Now, for example there are various subsets present in the Covid dataset, based on location, continent, etc. I am choosing location so that there can be a clear picture of what is being displayed and performed.



There are various parameters that you can plot against the date for this graph as you can see in the options.



I used a slightly old dataset for the first 2 graphs since you can see those end in May '21.





For the last 2 graphs, I used a newer dataset from the same source and you can see the graph tool works just fine and shows you numbers uptil June '21. Just did this to show that the graphs aren't inbuilt.





### Heatmap

For the heatmap it is evident that when we use CO2 data of countries, we can see trends as to which country is dedicated towards their climate goals and which ones are not. A few countries do not show a consistent trend (such as UAE) but for a lot of countries a visible pattern can be spotted. The CO2 dataset used by me was obtained from : https://github.com/owid/co2-data



It shows the CO2 growth in % of various countries and the colour of the box depends on the values present inside it, a very high value is bright (as you can see 44% is bright yellow) and the negative and lower values tend towards the blue colour, this can easily show you what number stands out instead of sitting and comparing these approx 100 numbers

### Stackplot



The last one I made is a stackplot, as the name makes it clear, it stacks the graphs on top of each other for you to have a better view of all the data, I used a few continents to draw this one since it showed in maximum clarity how it is beneficial, from this graph you can easily see that the global cases are at about 150 million at the end of April '21. and that North America and Asia have shown the most confirmed cases. If you are able to look a little closely you will also be able to spot the time of outbreaks in continents by how the thickness of the colour increases. (This was made in a slight hurry and the data is entered manually)


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
