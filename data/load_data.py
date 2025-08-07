import pandas as pd

def load_data():
    df = pd.read_csv('./data/data.csv', encoding='utf-8')
    numeric_cols = df.drop(['PatientId', 'AppointmentID', 'ScheduledDay', 'AppointmentDay'], axis=1).select_dtypes(['float64', 'int64'])
    return df, numeric_cols