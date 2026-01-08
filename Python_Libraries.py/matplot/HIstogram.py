import matplotlib.pyplot as plt
import numpy as np
#taking randon 100 value form 10and 30 
data=np.random.uniform(10,30,100)
#creating histogram
plt.figure(figsize=(8,6))
plt.hist(data,bins=40,color='blue',edgecolor='black')
plt.xlabel('value',color='black',labelpad=10,loc='center',fontsize=10,fontweight='bold')
plt.ylabel('frequency',color='black',labelpad=10,loc='center',fontsize=10,fontweight='bold')
plt.title('Histogram',color='red',fontsize=30,fontweight='bold')
plt.show()
