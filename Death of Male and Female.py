import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
a=pd.read_csv('D:\CODE\Saved\Death of Male and Female.csv')
x=np.linspace(1,83,10)
plt.xticks(x+3/2,['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','<90'])
plt.bar(x,a['f'],width=3,color='g',label='Female')
plt.bar(x+3,a['m'],width=3,color='b',label='Male')
plt.legend()
plt.xlabel('Age')
plt.ylabel('Number')
plt.title('No. of Deaths')
plt.show()
