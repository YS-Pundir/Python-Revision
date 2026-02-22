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

#Normalizing the dataset
norm=(dataset-nmean)/nstd

# psliting the dataset by 80 percent for training and the rest for testing 
ind=int(0.8*samples)

training_dataset=norm[:ind]
testing_dataset=norm[ind:]

print("Normalized dataset ")
print(norm)

print("training dataset")
print(training_dataset)

training_dataset[0,0]=5



# printing the orignal shape of dataset 
print("<>"*70)

print("Original Shape of Dataset : ",dataset.shape)
print("Mean shape:",nmean.shape)
print("Training data shape:",training_dataset.shape)
print("Test data shape:",testing_dataset.shape)
print("-"*20,"Note: Modifying the slice affected the original array","-"*20)

print("<>"*70)

print("-"*20," modified Normalized dataset ","-"*20)
print()
print(norm)
print()
print()
print("-"*20," modified training dataset","-"*20)
print()
print(training_dataset)









