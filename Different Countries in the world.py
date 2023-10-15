import matplotlib.pyplot as plt
import pandas as pd
a=pd.read_csv('D:\CODE\Saved\Different Countries in the world.csv')
plt.barh(a['n'],a['c'],color='r')
plt.title('Number of Covid-19 test performed in the most impacted countries Worldwide')
plt.xlabel('No. of test')
plt.ylabel('Country')
plt.show()
