import matplotlib.pyplot as plt
year=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
temp=[0.74,0.87,0.98,0.89,0.85,0.95,1.02,0.84,0.89,0.91,0.93]
plt.plot(year,temp)
plt.grid(True)
plt.title('Climate Change Data Analysis',loc='center',pad=20)
plt.xlabel('Year',labelpad=10,loc='center',color='red')
plt.ylabel('Global Tempratre Anomaly',labelpad=10,loc='center',color='red')

plt.show()
