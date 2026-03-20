import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

data = {
    "hours" : [1,2,3,4,5,6],
    "pass" : [0,0,0,1,1,1]
}

df = pd.DataFrame(data)
print(df)

X = df[["hours"]]
y = df["pass"]

model = LogisticRegression()
model.fit(X,y)

# res = model.predict([[30]])
# print(res[0])

# res = model.predict_proba([[3]])
# print(res[0])

plt.scatter(df["hours"],df["pass"])
plt.title("Student Pass/Fail Analysis")
plt.xlabel("Study Hours")
plt.ylabel("Pass")
plt.show()