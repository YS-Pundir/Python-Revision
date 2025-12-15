import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_xlabel('X-Label')
ax.set_ylabel('Y-Label')
ax.set_zlabel('Z-Label')
plt.show()
