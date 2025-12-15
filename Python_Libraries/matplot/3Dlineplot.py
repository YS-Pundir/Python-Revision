import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

x=[50,51,52,53,54,55,56,57,58]
y=[60,61,62,63,64,65,66,67,68]
z=[100,101,102,101,100,98,92,91,92]

ax.plot(x,y,z,color='black',marker='o')
ax.set_title("3D Line Chart",fontsize=20)
ax.set_xlabel('X-Label',fontweight='bold')
ax.set_ylabel('Y-Label',fontweight='bold')
ax.set_zlabel('Z-label',fontweight='bold')
ax.grid(True)
plt.show()