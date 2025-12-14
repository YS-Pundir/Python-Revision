import matplotlib.pyplot as plt
size=[20,30,20,20,10]
label=['a','b','c','d','e']
color=['blue','black','red','yellow','green']

plt.pie(size,labels=label,colors=color)
plt.title('Sample Pie Chart')
plt.show()