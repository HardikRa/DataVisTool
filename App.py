from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from plotGraphs import *

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

        home_button.place(x=5,y=10)

        plot_button = ttk.Button(self, command = lambda : plot_date_tick(self), text="Plot Graph")
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
        home_page.place(x=5,y=10)

        plot_button = ttk.Button(self, command = lambda : plot_heatmap(self), text="Plot Graph")
        plot_button.place(relx=0.5, rely= 0.15, anchor=CENTER)

        # country_selection_label=Label(self,text="Please select a country to draw a graph")
        # country_selection_label.place(relx = 0.5, rely = 0.4, anchor = CENTER)

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