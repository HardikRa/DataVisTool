from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

def plot_date_tick(parentClass):
    dataset_in_csv = pd.read_csv(r'owid-covid-data.csv')
    list_of_variables_in_dataset = list()
    for col in dataset_in_csv.columns:
        col_as_str = str(col)
        list_of_words_in_col = col_as_str.split('_')
        list_of_variables_in_dataset.append(" ".join(list_of_words_in_col).title())
    
    primary_key = dataset_in_csv.iso_code
    list_of_latest_entries = list()
    #To store the first index of a new tuple in the dataset
    first_entry = dict()
    #To store the last index of a new tuple in the dataset
    last_entry = dict()
    # list_of_countries=list()
    # count=0
    first_entry[str(dataset_in_csv.location[0])]=0
    list_of_latest_entries.append(0)
    for i in range(len(primary_key)-1):
        if (primary_key[i+1] != primary_key[i]):
            # count+=1
            first_entry[str(dataset_in_csv.location[i+1])]=i+1
            last_entry[str(dataset_in_csv.location[i])]=i
            #print(str(i)+'\t'+str(count)+'\t'+dataset_in_csv.location[i])
            # list_of_latest_entries.append(i)
            # list_of_countries.append(str(dataset_in_csv.location[i]))
    last_entry[str(dataset_in_csv.location[len(primary_key)-1])]=int(len(primary_key)-1)

    ## tuple_to_work_on=input("Enter the tuple you wish to work on:")
    tuple_to_work_on='India'
    date_stored=[np.datetime64(j) for j in dataset_in_csv.date[first_entry[tuple_to_work_on]:last_entry[tuple_to_work_on]+1]]

    x_axis=np.array(date_stored)

    y_axis=[(i) for i in dataset_in_csv.total_cases[first_entry[tuple_to_work_on]:last_entry[tuple_to_work_on]+1]]


    fig ,ax = plt.subplots()

    # ax.plot(x_axis,'total_cases',data=dataset_in_csv[first_entry[tuple_to_work_on]:last_entry[tuple_to_work_on]+1]) # +1 at the end so that the range function does consider the last entry of the tuple
    ax.plot(x_axis,y_axis)

    # import constants for the days of the week
    from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

    # tick on mondays every week
    fmt_week = mdates.WeekdayLocator(byweekday=MO)
    ax.xaxis.set_minor_locator(fmt_week)


    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()
    ax.xaxis.set_major_locator(fmt_month)
    fig.suptitle('Covid Dataset')
    plt.xlabel('Date')
    plt.ylabel('Number of total cases (India)')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))
    #fig.autofmt_xdate()
    #plt.figure(figsize=(800,200))
    plt.rc('xtick',labelsize=6)
    # plt.show()

    canvas = FigureCanvasTkAgg(fig, parentClass)
    canvas.draw()

    canvas.get_tk_widget().place(relx= 0.5, rely = 0.65, anchor= CENTER)

    #toolbar = NavigationToolbar2Tk(canvas, parentClass)
    #toolbar.update()

    canvas._tkcanvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)

