import numpy as np

# settigna random seed for better reproduciblity
np.random.seed(42)

#generating dataset as required in assignment using numpy
#samples are number of rows
samples=100
#features are number of columns
features=5

dataset=np.random.random((samples,features))

# Calculating the mean of features in dataset
nmean=np.mean(dataset,axis=0)
# i used axis=0 because it will make compilar to read from up to downside in every column one by one

# standard deviation calculation as asked in assignment 
nstd=np.std(dataset,axis=0)




