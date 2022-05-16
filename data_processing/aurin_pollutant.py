# Author:      Leqi Wang
# Student id:  1126066
# Description: preprocess pollutant data
import pandas as pd
import numpy as np
import json

def process_pollutant(data):

    pollutant = pd.read_csv(data)
    pollutant = pollutant.dropna(axis=0, subset=[' air_total_emission_kg']) ## drop nan
    inner_melbourne_list = ['Carlton', 'Carlton North', 'Docklands', 'East Melbourne', 
    'Flemington', 'Jolimont', 'Kensington', 'Melbourne', 'North Melbourne', 'Port Melbourne',
    'Parkville','Southbank','South Wharf','South Yarra', 'West Melbourne'
    ]
    
    output = dict()
    for suburb in inner_melbourne_list:
        count = pollutant.loc[pollutant[' suburb'] == suburb, ' air_total_emission_kg'].sum()
    
        output[suburb] = int(count)
    
    marklist = sorted(output.items(), key=lambda x:x[1], reverse = True)
    sortdict = dict(marklist)
    
    return sortdict

# pollutant = process_pollutant('pollutant.csv')
    
    
    
    


