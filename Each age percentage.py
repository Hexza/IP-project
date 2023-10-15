import matplotlib.pyplot as plt
import pandas as pd
a=pd.read_csv('D:\CODE\Saved\Each age percentage.csv')
plt.plot(a['x'],a['y'],marker='*',markeredgecolor='r')
plt.title('% of Death in each age group')
plt.xlabel('Ages')
plt.ylabel('Percent')
plt.show()
