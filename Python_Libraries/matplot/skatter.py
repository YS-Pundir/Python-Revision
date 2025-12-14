import matplotlib.pyplot as plt
import numpy as np
x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y,color='red',marker='*',alpha=0.5)#alpha is for the density of dots in scatter 
plt.xlabel('X-axis',fontdict={'fontsize': 14, 'fontweight': 'bold'},loc='center',color='red',labelpad=10)
plt.ylabel('Y-axis ',fontdict={'fontsize': 14, 'fontweight': 'bold'},loc='center',color='red',labelpad=10)
plt.title('scatter',loc='center',pad='10',fontsize=10,fontweight='bold',color='grey')
plt.show()
