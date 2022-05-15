import pandas as pd

def process_hospital_data():
    data = pd.DataFrame()
    df = pd.read_csv('../data/hospital.csv')
    df.groupby("suburb").agg(
    b_min=pd.NamedAgg(column="B", aggfunc="min"),
    c_sum=pd.NamedAgg(column="C", aggfunc="sum"))
    print(df)

process_hospital_data()