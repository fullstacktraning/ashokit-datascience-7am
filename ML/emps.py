# emps data. 1y - 3lakh, 2-5lakh, 3-7lakh, 4y --- ?
# numpy - mathematical calculations
import numpy as np
# matplotlib - used to draw the graphs
import matplotlib.pyplot as plt
# import LinearRegression (y=mX + b)
from sklearn.linear_model import LinearRegression
# train_test_split, used to split the data 1) Training 2) Testing
from sklearn.model_selection import train_test_split # [10,20,30,40,50,60] --- 80% Training. 20% Testing 

#Features (emps experience)
X = np.array([1,2,3,4,5]).reshape(-1,1)   #Training. Testing. 

#label (salary)
y = np.array([3,5,7,9,11])

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

new_exp = [[6]]
salary = model.predict(new_exp)
print("Salary for 6 Years :",salary[0])

plt.scatter(X,y,color="red")
plt.scatter(new_exp,salary,color="blue")
plt.plot(X,y,color="yellow")
plt.show()

