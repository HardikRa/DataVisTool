from tkinter import *
import tkinter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

dataset_in_csv = pd.core.frame.DataFrame()

def open_csv_file():
    globals()['dataset_in_csv'] = pd.read_csv(tkinter.filedialog.askopenfile(mode = 'r', filetypes = [('CSV Datasets','*.csv')]))

def list_of_var():
    list_of_variables_in_dataset = list()
    for col in dataset_in_csv.columns:
        col_as_str = str(col)
        list_of_words_in_col = col_as_str.split('_')
        list_of_variables_in_dataset.append(" ".join(list_of_words_in_col).title())
    return list_of_variables_in_dataset

#primary key is unique for every subset
def list_of_subset(pk):
    list_of_subsets_possible = list()
    list_of_subsets_possible = [str(x) for x in dataset_in_csv[pk] if x not in list_of_subsets_possible ]    
    return list_of_subsets_possible

def plot_date_tick(parentClass, pk, subset_of_data, parameter_on_y):
    #dataset_in_csv = pd.read_csv(r'owid-covid-data.csv')
    
    primary_key = dataset_in_csv[pk]
    list_of_latest_entries = list()
    #To store the first index of a new tuple in the dataset
    first_entry = dict()
    #To store the last index of a new tuple in the dataset
    last_entry = dict()
    # list_of_countries=list()
    # count=0
    first_entry[str(dataset_in_csv[pk][0])]=0
    list_of_latest_entries.append(0)
    for i in range(len(primary_key)-1):
        if (primary_key[i+1] != primary_key[i]):
            # count+=1
            first_entry[str(dataset_in_csv[pk][i+1])]=i+1
            last_entry[str(dataset_in_csv[pk][i])]=i
            #print(str(i)+'\t'+str(count)+'\t'+dataset_in_csv[pk][i])
            # list_of_latest_entries.append(i)
            # list_of_countries.append(str(dataset_in_csv[pk][i]))
    last_entry[str(dataset_in_csv[pk][len(primary_key)-1])]=int(len(primary_key)-1)

    ## subset_of_data=input("Enter the tuple you wish to work on:")
    #subset_of_data='India'
    date_stored=[np.datetime64(j) for j in dataset_in_csv.date[first_entry[subset_of_data]:last_entry[subset_of_data]+1]]

    x_axis=np.array(date_stored)

    y_axis=[(i) for i in dataset_in_csv[parameter_on_y][first_entry[subset_of_data]:last_entry[subset_of_data]+1]]
    list_of_words_in_y_parameter = parameter_on_y.split('_')
    y_parameter_for_label = " ".join(list_of_words_in_y_parameter).title()

    fig ,ax = plt.subplots()

    # ax.plot(x_axis,'[parameter_on_y]',data=dataset_in_csv[first_entry[subset_of_data]:last_entry[subset_of_data]+1]) # +1 at the end so that the range function does consider the last entry of the tuple
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
    plt.ylabel('Number of ' + y_parameter_for_label + ' ('+ subset_of_data +')')
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

    canvas._tkcanvas.place(relx = 0.5, rely = 0.65, anchor = CENTER)

def plot_heatmap(parentClass,pk,list_on_y, no_of_columns_on_x):
    # dataset_in_csv = pd.read_csv(r'owid-co2-data.csv')
    primary_key = dataset_in_csv[pk]
    list_of_latest_entries = list()
    #To store the first index of a new tuple in the dataset
    first_entry = dict()
    #To store the last index of a new tuple in the dataset
    last_entry = dict()
    # list_of_countries=list()
    # count=0
    first_entry[str(dataset_in_csv[pk][0])]=0
    list_of_latest_entries.append(0)
    for i in range(len(primary_key)-1):
        if (primary_key[i+1] != primary_key[i]):
            # count+=1
            first_entry[str(dataset_in_csv[pk][i+1])]=i+1
            last_entry[str(dataset_in_csv[pk][i])]=i
            #print(str(i)+'\t'+str(count)+'\t'+dataset_in_csv[pk][i])
            # list_of_latest_entries.append(i)
            # list_of_countries.append(str(dataset_in_csv[pk][i]))
    last_entry[str(dataset_in_csv[pk][len(primary_key)-1])]=int(len(primary_key)-1)
    # list_on_y = ['Russia','India','Spain','France','Japan','Kuwait','United Arab Emirates','Sweden','Turkey','United States','United Kingdom']
    values_list = list()
    x_key='year'
    #n=10
    for key in list_on_y:
        values_list.append([float(i) for i in dataset_in_csv['co2_growth_prct'][last_entry[key]-no_of_columns_on_x+1:last_entry[key]+1]])

    values = np.array(values_list)
    x_values=[x for x in dataset_in_csv[x_key][last_entry[key]-no_of_columns_on_x+1:last_entry[key]+1]]

    fig,ax = plt.subplots()
    # plt.figure(figsize=(110,200))
    im1=ax.imshow(values)
    ax.set_xticks(np.arange(len(x_values)))
    ax.set_yticks(np.arange(len(list_on_y)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(x_values)
    ax.set_yticklabels(list_on_y)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(list_on_y)):
        for j in range(len(x_values)):
            # print(i)
            # print(j)
            # print()
            text = ax.text(j, i, values[i, j],
                        ha="center", va="center", color="w",fontsize=6)

    ax.set_title("% in CO2 rise Year on Year for various countries")
    #fig.tight_layout()
    #plt.show()
    canvas = FigureCanvasTkAgg(fig, parentClass)
    canvas.draw()

    canvas.get_tk_widget().place(relx= 0.5, rely = 0.65, anchor= CENTER)

    #toolbar = NavigationToolbar2Tk(canvas, parentClass)
    #toolbar.update()

    canvas._tkcanvas.place(relx = 0.5, rely = 0.65, anchor = CENTER)
