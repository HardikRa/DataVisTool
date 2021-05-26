from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

def plot_date_tick():
    dataset_in_csv = pd.read_csv('owid-covid-data (1).csv')

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

    tuple_to_work_on=input("Enter the tuple you wish to work on:")
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
    canvas = FigureCanvasTkAgg(fig, master = Date_tick_Page)
    canvas.draw()

    canvas.get_tk_widget().place(relx= 0.5, rely = 0.75, anchor= CENTER)

    toolbar = NavigationToolbar2Tk(canvas, Date_tick_Page)
    toolbar.update()
    
    canvas.get_tk_widget().place(relx= 0.5, rely = 0.75, anchor= CENTER)
    
class tkinterApp(Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        self.title("DataVis Tool")
        self.geometry('800x450')
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Entry_Page, Date_tick_Page, Heatmap_Page, BarGraph_Page, StackPlot_Page):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Entry_Page)
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Entry_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Welcome to DataVis Tool!")
         
        # putting the grid in its place by using
        # grid
        label.place(relx = 0.5, rely = 0.05, anchor = CENTER)
  
        date_tick_button = ttk.Button(self, text ="Date Tick Graph",
        command = lambda : controller.show_frame(Date_tick_Page))
     
        # putting the button in its place by
        # using grid
        date_tick_button.place(relx = 0.5, rely = 0.15, anchor = CENTER)
  
        ## button to show frame 2 with text layout2
        heatmap_button = ttk.Button(self, text ="Heatmap Graph",
        command = lambda : controller.show_frame(Heatmap_Page))
     
        # putting the button in its place by
        # using grid
        heatmap_button.place(relx = 0.5, rely = 0.25, anchor = CENTER) 

        #making a button for BarGraph_Page
        bar_graph_button = ttk.Button(self, text = "Bar Graph",
        command = lambda : controller.show_frame(BarGraph_Page))

        bar_graph_button.place(relx = 0.5, rely = 0.35, anchor = CENTER)

        #creating button for Stackplot
        stackplot_button = ttk.Button(self, text = "Stackplot",
        command = lambda : controller.show_frame(StackPlot_Page))

        stackplot_button.place(relx = 0.5, rely = 0.45, anchor = CENTER)

class Date_tick_Page(Frame):
     
    def __init__(self, parent, controller):
         
        Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Date Tick Graph")
        label.place(relx = 0.5, rely = 0.05, anchor = CENTER)
  
        # button to show frame 2 with text
        # layout2
        home_button = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Entry_Page))
     
        # putting the button in its place
        # by using grid

        home_button.grid(row = 0, column = 0, padx = 5, pady = 0)

        plot_button = Button(master = Date_tick_Page, command = plot_date_tick, height = 2, width= 10, text="Plot Graph")
        plot_button.place(relx=0.5, rely= 0.15, anchor=CENTER)
        # country_selection_label=Label(self,text="Please select a country to draw a graph")
        # country_selection_label.grid(row=2, column=1, padx=20, pady=20)

        # country_selected=StringVar()

        # country_selection_dropdown=ttk.Combobox(self,width=20,textvariable=country_selected)
        # country_selection_dropdown['values']=('Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'European Union', 'Faeroe Islands', 'Falkland Islands', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'International', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North America', 'North Macedonia', 'Northern Cyprus', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turks and Caicos Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Vietnam', 'World', 'Yemen', 'Zambia')
        # country_selection_dropdown.grid(row=2,column=3,padx=0, pady=20)
        # country_selection_dropdown.current(0)

        # graphtype_selection_label=Label(self,text="Select the graphtype: ")
        # graphtype_selection_label.grid(row=4,column=1, padx=20, pady=20)

        # graphtype_selected=StringVar()

        # graphtype_selection_dropdown=ttk.Combobox(self,width=10,textvariable=graphtype_selected)
        # graphtype_selection_dropdown['values']=['Date-Tick', 'Heatmap']
        # graphtype_selection_dropdown.grid(row=4, column=3, padx=0, pady=20)
        # graphtype_selection_dropdown.current(0)
        # button to show frame 2 with text
        # layout2
        # button2 = ttk.Button(self, text ="Page 2",
        #                     command = lambda : controller.show_frame(Heatmap_Page))
     
        # # putting the button in its place by
        # # using grid
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)
class Heatmap_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Heatmap Graph",)
        label.place(relx = 0.5, rely = 0.05, anchor = CENTER)
  
        # button to show frame 2 with text
        # layout2
        home_page = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Entry_Page))
     
        # putting the button in its place by
        # using grid
        home_page.grid(row = 0, column = 0, padx = 5, pady = 10)


        country_selection_label=Label(self,text="Please select a country to draw a graph")
        country_selection_label.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        country_selected=StringVar()

        country_selection_dropdown=ttk.Combobox(self,width=20,textvariable=country_selected)
        country_selection_dropdown['values']=('Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'European Union', 'Faeroe Islands', 'Falkland Islands', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'International', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North America', 'North Macedonia', 'Northern Cyprus', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turks and Caicos Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Vietnam', 'World', 'Yemen', 'Zambia')
        country_selection_dropdown.grid(row=2,column=3,padx=0, pady=20)
        country_selection_dropdown.current(0)

        graphtype_selection_label=Label(self,text="Select the graphtype: ")
        graphtype_selection_label.grid(row=4,column=1, padx=20, pady=20)

        graphtype_selected=StringVar()

        graphtype_selection_dropdown=ttk.Combobox(self,width=10,textvariable=graphtype_selected)
        graphtype_selection_dropdown['values']=['Date-Tick', 'Heatmap']
        graphtype_selection_dropdown.grid(row=4, column=3, padx=0, pady=20)
        # button to show frame 3 with text
        # layout3
        # button2 = ttk.Button(self, text ="Startpage",
        #                     command = lambda : controller.show_frame(StartPage))
     
        # # putting the button in its place by
        # # using grid
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)
class BarGraph_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Bar Graph")
        label.place(relx = 0.5, rely = 0.05, anchor = CENTER)

        #button to go to home page
        home_page = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Entry_Page))
        
        home_page.grid(row = 0, column = 0, padx= 5, pady = 10)

class StackPlot_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Stack Plot")
        label.place(relx = 0.5, rely = 0.05, anchor = CENTER)

        #button to go to home page
        home_page = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Entry_Page))
        
        home_page.grid(row = 0, column = 0, padx= 5, pady = 10)


app = tkinterApp()
app.mainloop()