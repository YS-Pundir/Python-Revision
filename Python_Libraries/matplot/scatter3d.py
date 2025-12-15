import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
bx=fig.add_subplot(777,projection='3d')

longitude=[50,51,52,53,54,55,56,57,58]
latitude=[61,62,63,64,65,66,67,68,69]
elevation=[100,101,102,103,104,105,106,91,92]

ax.scatter(longitude,latitude,elevation,color='blue')
ax.set_title('3D visulisation')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('elevation')
ax.grid(True)

x=[1,3,2,4,45,56,4,32,66,54,32,2]
y=[4,5,3,2,5,3,6,4,33,3,2,2]
z=[1,5,4,6,4,3,3,2,3,3,4,7]

bx.set_xlabel('X-axis')
bx.set_ylabel('Y-axis')
bx.set_zlabel('Z-axis')
bx.set_title('3d Data visualisation',color='black',fontsize=30,fontweight='bold')

bx.scatter(x,y,z,color='black')

plt.show()