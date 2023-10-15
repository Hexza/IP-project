import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
a=pd.read_csv('D:\CODE\Saved\Least affected cities.csv')
x=np.linspace(1,90,5)
plt.xticks(x+8/2,['Rajnandgaon','Durg','Baloda Bazar','Raigarh','Bijapur'])
plt.bar(x,a['Confirmed Cases'],width=3,color='blue',label='Confirmed')
plt.bar(x+3,a['Recovered Cases'],width=3,color='green',label='Recovered')
plt.bar(x+6,a['Death cases'],width=3,color='red',label='Death')
plt.bar(x+9,a['Active Cases'],width=3,color='yellow',label='Active Cases')
plt.title('Least affected cities from Covid-19 in Chhattisgarh')
plt.legend()
plt.xlabel('Cities')
plt.ylabel('Number')
plt.show()
