import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y)
plt.grid()
plt.xlabel("X-axis",color='blue',labelpad=10)
plt.ylabel("y-axis",color='blue',labelpad=10)
plt.title("Simple Line Plot")
plt.text(3,15,"#",fontsize=10,color='blue')
plt.show()