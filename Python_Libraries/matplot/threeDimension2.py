import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

x=[1,3,2,4,45,56,4,32,66,54,32,2]
y=[4,5,3,2,5,3,6,4,33,3,2,2]
z=[1,5,4,6,4,3,3,2,3,3,4,7]

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3d Data visualisation',color='black',fontsize=30,fontweight='bold')

ax.scatter(x,y,z,color='black')

plt.show()