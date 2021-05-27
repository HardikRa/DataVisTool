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
        for F in (Entry_Page, Date_tick_Page, Heatmap_Page, StackPlot_Page):
  
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
     
        # putting the button in its place by using place
        date_tick_button.place(relx = 0.5, rely = 0.15, anchor = CENTER)
  
        ## button to show frame 2 with text layout2
        heatmap_button = ttk.Button(self, text ="Heatmap Graph",
        command = lambda : controller.show_frame(Heatmap_Page))
     
        # putting the button in its place by using place
        heatmap_button.place(relx = 0.5, rely = 0.25, anchor = CENTER) 

        #creating button for Stackplot
        stackplot_button = ttk.Button(self, text = "Stackplot",
        command = lambda : controller.show_frame(StackPlot_Page))

        stackplot_button.place(relx = 0.5, rely = 0.35, anchor = CENTER)

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

        home_button.place(x=5,y=10)

        open_file_button = ttk.Button(self, text = "Open a file", command = lambda : open_csv_file() )
        open_file_button.place(relx = 0.7, rely = 0.1, anchor=CENTER)

        #User-input space
        primary_key_label = Label(self, text="Please select a column that will differentiate subsets")
        primary_key_label.place(relx = 0.25, rely = 0.15, anchor=CENTER)

        primary_key = StringVar()

        primary_key_dropdown = ttk.Combobox(self,width=10, textvariable=primary_key)
        primary_key_dropdown['values'] = ('Iso Code', 'Continent', 'Location', 'Date', 'Total Cases', 'New Cases', 'New Cases Smoothed', 'Total Deaths', 'New Deaths', 'New Deaths Smoothed', 'Total Cases Per Million', 'New Cases Per Million', 'New Cases Smoothed Per Million', 'Total Deaths Per Million', 'New Deaths Per Million', 'New Deaths Smoothed Per Million', 'Reproduction Rate', 'Icu Patients', 'Icu Patients Per Million', 'Hosp Patients', 'Hosp Patients Per Million', 'Weekly Icu Admissions', 'Weekly Icu Admissions Per Million', 'Weekly Hosp Admissions', 'Weekly Hosp Admissions Per Million', 'New Tests', 'Total Tests', 'Total Tests Per Thousand', 'New Tests Per Thousand', 'New Tests Smoothed', 'New Tests Smoothed Per Thousand', 'Positive Rate', 'Tests Per Case', 'Tests Units', 'Total Vaccinations', 'People Vaccinated', 'People Fully Vaccinated', 'New Vaccinations', 'New Vaccinations Smoothed', 'Total Vaccinations Per Hundred', 'People Vaccinated Per Hundred', 'People Fully Vaccinated Per Hundred', 'New Vaccinations Smoothed Per Million', 'Stringency Index', 'Population', 'Population Density', 'Median Age', 'Aged 65 Older', 'Aged 70 Older', 'Gdp Per Capita', 'Extreme Poverty', 'Cardiovasc Death Rate', 'Diabetes Prevalence', 'Female Smokers', 'Male Smokers', 'Handwashing Facilities', 'Hospital Beds Per Thousand', 'Life Expectancy', 'Human Development Index')
        primary_key_dropdown.place(relx = 0.25, rely =0.2, anchor=CENTER)
        

        subset_selection_label = Label(self, text="Select the subset you would like to work on")
        subset_selection_label.place(relx= 0.65, rely = 0.15, anchor=CENTER)

        subset_selection = StringVar()
        subset_selection_dropdown = ttk.Combobox(self, width =25,textvariable=subset_selection)
        #subset_selection_dropdown['values'] = tuple(list_of_subset('location'))
        subset_selection_dropdown['values'] = ('Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'European Union', 'Faeroe Islands', 'Falkland Islands', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'International', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North America', 'North Macedonia', 'Northern Cyprus', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turks and Caicos Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Vietnam', 'World', 'Yemen', 'Zambia', 'Zimbabwe')
        subset_selection_dropdown.place(relx = 0.65, rely = 0.2, anchor=CENTER)

        y_parameter_label = Label(self, text="Enter the parameter you would like to plot along the y-axis")
        y_parameter_label.place(relx=0.5, rely = 0.45,anchor=CENTER)
        y_parameter = StringVar()
        y_parameter_dropdown = ttk.Combobox(self, width=20, textvariable=y_parameter)
        y_parameter_dropdown['values'] = ('Iso Code', 'Continent', 'Location', 'Date', 'Total Cases', 'New Cases', 'New Cases Smoothed', 'Total Deaths', 'New Deaths', 'New Deaths Smoothed', 'Total Cases Per Million', 'New Cases Per Million', 'New Cases Smoothed Per Million', 'Total Deaths Per Million', 'New Deaths Per Million', 'New Deaths Smoothed Per Million', 'Reproduction Rate', 'Icu Patients', 'Icu Patients Per Million', 'Hosp Patients', 'Hosp Patients Per Million', 'Weekly Icu Admissions', 'Weekly Icu Admissions Per Million', 'Weekly Hosp Admissions', 'Weekly Hosp Admissions Per Million', 'New Tests', 'Total Tests', 'Total Tests Per Thousand', 'New Tests Per Thousand', 'New Tests Smoothed', 'New Tests Smoothed Per Thousand', 'Positive Rate', 'Tests Per Case', 'Tests Units', 'Total Vaccinations', 'People Vaccinated', 'People Fully Vaccinated', 'New Vaccinations', 'New Vaccinations Smoothed', 'Total Vaccinations Per Hundred', 'People Vaccinated Per Hundred', 'People Fully Vaccinated Per Hundred', 'New Vaccinations Smoothed Per Million', 'Stringency Index', 'Population', 'Population Density', 'Median Age', 'Aged 65 Older', 'Aged 70 Older', 'Gdp Per Capita', 'Extreme Poverty', 'Cardiovasc Death Rate', 'Diabetes Prevalence', 'Female Smokers', 'Male Smokers', 'Handwashing Facilities', 'Hospital Beds Per Thousand', 'Life Expectancy', 'Human Development Index')
        y_parameter_dropdown.place(relx = 0.5, rely = 0.25,anchor= CENTER)

        #plot_button = ttk.Button(self, command = lambda : plot_date_tick(self,'location','India','Total Cases'), text="Plot Graph")
        plot_button = ttk.Button(self, command = lambda : plot_date_tick(self,str(primary_key.get()).lower(),str(subset_selection.get()),str(y_parameter.get()).lower()), text="Plot Graph")
        plot_button.place(relx=0.5, rely= 0.35, anchor=CENTER)
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

        open_file_button = ttk.Button(self, text = "Open a file", command = lambda : open_csv_file() )
        open_file_button.place(relx = 0.7, rely = 0.1, anchor=CENTER)

        # User-input space

        inform_label=Label(self,text="This graph will plot rise in CO2 as a heatmap for the selected countries")
        inform_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

        country_selected_index=list()

        country_selection_list = ['Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Asia (excl. China & India)', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'EU-27', 'EU-28', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'Europe (excl. EU-27)', 'Europe (excl. EU-28)', 'Faeroe Islands', 'Fiji', 'Finland', 'France', 'French Equatorial Africa', 'French Polynesia', 'French West Africa', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'International transport', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kuwaiti Oil Fires', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Leeward Islands', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North America', 'North America (excl. USA)', 'North Korea', 'North Macedonia', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Panama Canal Zone', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Ryukyu Islands', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts-Nevis-Anguilla', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis and Futuna Islands', 'World', 'Yemen', 'Zambia', 'Zimbabwe']
        country_selection_listbox= Listbox(self,width=20,selectmode=MULTIPLE,listvariable=country_selection_list)
        for each_item in range(len(country_selection_list)):
            country_selection_listbox.insert(END, country_selection_list[each_item])
        

        country_selection_listbox.place(relx=0.25, rely=0.25, anchor=CENTER)
        # country_selection_dropdown.current(0)
        country_selected=list()
        
        def list_sel_countries():
            for x in country_selection_listbox.curselection():
                country_selected.append(country_selection_listbox.get(x))
        plot_button = ttk.Button(self, command = lambda : plot_heatmap(self,'country',['Russia','India','Spain','France','Japan','Kuwait','United Arab Emirates','Sweden','Turkey','United States','United Kingdom'],10,'co2_growth_prct'), text="Plot Graph")
        
        confirm_selection_button = ttk.Button(self, text="Confirm Choices", command= lambda : list_sel_countries)
        confirm_selection_button.place(relx = 0.25, rely = 0.1, anchor= CENTER)


        
        #plot_button = ttk.Button(self, command = lambda : controller.show_frame(Heatmap_Page1), text="Plot Graph")
        plot_button.place(relx=0.5, rely= 0.35, anchor=CENTER)

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

# class Heatmap_Page1(Heatmap_Page):
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         label = ttk.Label(self, text ="Heatmap Graph",)
#         label.place(relx = 0.5, rely = 0.05, anchor = CENTER)
  
#         # button to show frame 2 with text
#         # layout2
#         home_page = ttk.Button(self, text ="Home",
#                             command = lambda : controller.show_frame(Entry_Page))
     
#         # putting the button in its place by
#         # using grid
#         home_page.place(x=5,y=10)

#         open_file_button = ttk.Button(self, text = "Open a file", command = lambda : open_csv_file() )
#         open_file_button.place(relx = 0.7, rely = 0.1, anchor=CENTER)

#         # User-input space

#         inform_label=Label(self,text="This graph will plot rise in CO2 as a heatmap for the selected countries")
#         inform_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

#         country_selected_index=list()

#         country_selection_list = ['Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Asia (excl. China & India)', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'EU-27', 'EU-28', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'Europe (excl. EU-27)', 'Europe (excl. EU-28)', 'Faeroe Islands', 'Fiji', 'Finland', 'France', 'French Equatorial Africa', 'French Polynesia', 'French West Africa', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'International transport', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kuwaiti Oil Fires', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Leeward Islands', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North America', 'North America (excl. USA)', 'North Korea', 'North Macedonia', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Panama Canal Zone', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Ryukyu Islands', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts-Nevis-Anguilla', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis and Futuna Islands', 'World', 'Yemen', 'Zambia', 'Zimbabwe']
#         country_selection_listbox= Listbox(self,width=20,selectmode=MULTIPLE,listvariable=country_selection_list)
#         for each_item in range(len(country_selection_list)):
#             country_selection_listbox.insert(END, country_selection_list[each_item])

#         plot_button = ttk.Button(self, command = lambda : plot_heatmap(self,'country',super.country_selected,10,'co2_growth_prct'), text="Plot Graph")
#         plot_button.place(relx = 0.5, rely = 0.35, anchor= CENTER)

        
class StackPlot_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Stack Plot")
        label.place(relx = 0.5, rely = 0.05, anchor = CENTER)

        #button to go to home page
        home_page = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Entry_Page))
        
        home_page.place(x = 5, y = 10)

        open_file_button = ttk.Button(self, text = "Open a file", command = lambda : open_csv_file() )
        open_file_button.place(relx = 0.6, rely = 0.1, anchor=CENTER)

        plot_button = ttk.Button(self, command = lambda : plot_stack_plot(self), text="Plot Graph")
        plot_button.place(relx=0.5, rely= 0.35, anchor=CENTER)


app = tkinterApp()
app.mainloop()