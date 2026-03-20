#import numpy
#used to work with lists
import numpy as np
#import pyplot
#pyplot used to draw graphs
import matplotlib.pyplot as plt
#import LinearRegression (y =mX + c)
from sklearn.linear_model import LinearRegression
# define Features
# 2D shape
# reshape(). 1D - 2D
X = np.array([1,2,3,4,5]).reshape(-1,1)
# define labels
y = np.array([10,20,30,40,50])
# choose the model
model = LinearRegression()
# train the model
model.fit(X,y)
# test the model (predixt)
sample = [[10]]
marks = model.predict(sample)
print(marks[0])
plt.scatter(X,y,color="blue")
plt.scatter(sample,marks,color="green")
plt.plot(X,y,color="red")
plt.show()