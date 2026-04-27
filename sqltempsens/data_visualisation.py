import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
now=datetime.now()
formatted_now = now.strftime("%Y%m%d_%H'%M'%S")

data_csv="2601421_messdata_10000.csv"

#%%
data = pd.read_csv(data_csv, header="infer")
print(data.head())
print(data.shape)

data['Messzeit'] = pd.to_datetime(data['Messzeit'])
data['Luftfeuchte'] = data['Luftfeuchte'].str.replace(",",".").astype(float)
data['Temperatur'] = data['Temperatur'].str.replace(",",".").astype(float)
data['Druck'] = data['Druck'].str.replace(",",".").astype(float)

locations = data['StandortID'].unique()
data_by_loca = {}

for location in locations:
    temp_data = data[data['StandortID'] == location].reset_index(drop=True)
    print(temp_data.head())
    print(temp_data.shape)
    # fertigen DataFrame im Dictionary abspeichern
    data_by_loca[location] = temp_data

#%%
for location in locations:
    x_if = None
    name = f'{formatted_now}_{location}.pdf'
    
    plt.figure()
    plt.plot('Messzeit', 'Temperatur', data=data_by_loca[location], label = "Temperatur")
    plt.plot('Messzeit', 'Druck', data=data_by_loca[location], label = "Druck")
    plt.plot('Messzeit', 'Luftfeuchte', data=data_by_loca[location], label = "Luftfeuchte")
    plt.legend()
    plt.title(f'{formatted_now} - {location}')
    plt.show()
    
    while x_if != "y" and x_if != "n":
        x_if = input(f'{name}\nPlotausgabe als Datei? [y/n]').lower()
    if x_if == "y":
        plt.savefig(name, format="pdf")

    
