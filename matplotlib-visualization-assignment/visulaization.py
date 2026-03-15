import numpy as np
import matplotlib.pyplot as pip

epochs=np.arange(1,11)
loss=np.random.rand(10)

pip.figure()
pip.plot(epochs,loss,marker="s",linestyle=":",markerfacecolor="black")
pip.title("Line Plot",color="red",fontweight="bold")
pip.xlabel("Epochs",color="Blue",fontweight="bold")
pip.ylabel("Loss value",color="Blue",fontweight="bold")
pip.grid(True)
pip.legend()
pip.show()

pip.figure()
pip.scatter(epochs,loss,marker="*")
pip.title("Scatter Plot",color="red",fontweight="bold")
pip.xlabel("Epochs",color="Blue",fontweight="bold")
pip.ylabel("Loss value",color="Blue",fontweight="bold")
pip.grid(True)
pip.show()

x=["Model A","Model B","Model C"]
y=[0.85,0.90,0.88]
pip.figure()
pip.bar(x,y,color=["Red","Green","Blue"])
pip.xlabel("Models",fontweight="bold",color="Black")
pip.ylabel("Accuracy",fontweight="bold",color="Black")
pip.title("Accuracy Bar Chart",color="red",fontweight="bold",fontsize=40)
pip.grid(True)
pip.show()