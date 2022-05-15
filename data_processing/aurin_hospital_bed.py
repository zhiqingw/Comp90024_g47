import pandas as pd
import numpy as np
import json

def process_hospital(data):

    hospital = pd.read_csv(data)
    hospital = hospital.dropna(axis=0, subset=[' beds']) ## drop nan
    inner_melbourne_list = ['Carlton', 'Carlton North', 'Docklands', 'East Melbourne', 
    'Flemington', 'Jolimont', 'Kensington', 'Melbourne', 'North Melbourne', 'Port Melbourne',
    'Parkville','Southbank','South Wharf','South Yarra', 'West Melbourne'
    ]
    
    
    bed_counts = list(hospital[' beds'].unique())
    
    avg_bed_counts = {'<50': 25, '50-99': 75, '100-199': 150, '>500': 500, '200-500': 350}
    hospital['avg_beds'] = hospital[' beds'].map(lambda x: avg_bed_counts[x])
    output = dict()
    for suburb in list(inner_melbourne_list):
        count = hospital.loc[hospital[' suburb'] == suburb, 'avg_beds'].sum()
    
        output[suburb] = int(count)
    
    marklist = sorted(output.items(), key=lambda x:x[1], reverse = True)
    sortdict = dict(marklist)
    
    
    return sortdict

# hospital = process_hospital('hospital.csv')
    
    
    
    


