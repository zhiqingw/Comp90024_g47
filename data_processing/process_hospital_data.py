import pandas as pd

def process_hospital_data():
    data = pd.DataFrame()
    df = pd.read_json("../data/hospital.json")
    print(df)

process_hospital_data()