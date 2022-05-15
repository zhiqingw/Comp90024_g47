import pandas as pd
import numpy as np
import json

def process_seat(data):

    seat = pd.read_csv(data)
    seat = seat.dropna(axis=0, subset=[' number_of_seats']) ## drop nan
    inner_melbourne_list = ['Carlton', 'Carlton North', 'Docklands', 'East Melbourne', 
    'Flemington', 'Jolimont', 'Kensington', 'Melbourne', 'North Melbourne', 'Port Melbourne',
    'Parkville','Southbank','South Wharf','South Yarra', 'West Melbourne'
    ]
    
    
    seat[' suburb'] = seat[' clue_small_area'].map(lambda x: x.replace('Melbourne (CBD)', 'Melbourne'))
    seat[' suburb'] = seat[' suburb'].map(lambda x: x.replace('West Melbourne (Industrial)', 'West Melbourne'))
    seat[' suburb'] = seat[' suburb'].map(lambda x: x.replace('West Melbourne (Residential)', 'West Melbourne'))
    
    output = dict()
    for suburb in inner_melbourne_list:
        count = seat.loc[seat[' suburb'] == suburb, ' number_of_seats'].sum()
        output[suburb] = int(count)
    
    marklist = sorted(output.items(), key=lambda x:x[1], reverse = True)
    sortdict = dict(marklist)
        
    return sortdict

seat = process_seat('seat.csv')
    
    
    
    


