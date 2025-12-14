import matplotlib.pyplot as plt

categories=['A','B','C','D','E']
values=[111,424,422,331,313]
plt.bar(categories,values,width=0.8,align='center')
plt.xlabel('Categories',color='green',fontsize=10,fontweight='bold',loc='center',labelpad=20)
plt.ylabel('values',color='green',fontsize=10,fontweight='bold',loc='center',labelpad=20)
plt.title('Simple Bar Chart',fontsize=40,color='black',pad=30)
plt.show()