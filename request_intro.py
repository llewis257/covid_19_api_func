# Importing required module to perform the task
import requests
import pandas as pd 
from pandas.io.json import json_normalize
import re
import numpy as np

class Cases(): 
    def __init__(self, json_dt):
        self.json_data = json_dt
    def spec_country_avg(self, country):
        for c in self.json_data['Country']:
            if c == country:
                covid_data = pd.read_json('https://api.covid19api.com/country/' + c.replace(' ', '-'))
                #print(covid_data)## data from the json file  ['ID', 'Country', 'CountryCode', 'Province', 'City', 'CityCode', 'Lat', 'Lon', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Date']
                toprint = covid_data[['Country', 'Confirmed', 'Deaths', 'Date']]
                print(toprint)
    def all_average_cases(self):
        #iterating through all available countries
        for c in self.json_data['Country']:
            covid_data = pd.read_json('https://api.covid19api.com/country/' + c.replace(' ', '-'))
            #print(covid_data)## data from the json file  ['ID', 'Country', 'CountryCode', 'Province', 'City', 'CityCode', 'Lat', 'Lon', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Date']
            toprint = covid_data[['Country', 'Confirmed', 'Deaths', 'Date']]
            print(toprint)
    def fatalities_day(self, g_country, g_day):
        spec_country = pd.read_json('https://api.covid19api.com/country/' + g_country.replace(' ', '-'))
        fatal = None
        g_date = str(g_day + ' ' + '00:00:00+00:00')
        for _, d in spec_country.iterrows():
            if (str(d['Date']) == g_date):
                fatal = d['Deaths']
                return fatal
            # print(d)
            # print(spec_country[['Country', 'Deaths', 'Date']])
            # fatal = spec_country['Deaths']
        
        #return fatal

if __name__== "__main__":
    main_json_data = pd.read_json('https://api.covid19api.com/countries')
    cases = Cases(main_json_data)
    ## uncomment next line to find out the average cases from given country 
    #cases.spec_country_avg(country='Burundi')

    ##uncomment next line to find out all average cases from all available countries
    ## P.S There'll be an error after too many requests
    #cases.all_average_cases()

    
    i_country= input('Enter 1 specific country:\n ->')
    i_date = input('Enter One specific date in the format YYYY-MM-DD\n ->')
    print(f'fatalities in {i_country} on date {i_date} are {cases.fatalities_day(i_country, i_date)}')
