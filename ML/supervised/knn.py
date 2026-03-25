from sklearn.neighbors import KNeighborsClassifier
# read from excel sheet
X = [[150,50],[160,55],[170,65],[180,80],[175,75]]
y = ["Slim","Slim","Fit","Heavy","Heavy"]
model = KNeighborsClassifier(n_neighbors=4) 
model.fit(X,y)
# swagger
res = model.predict([[165,60]])
# return res
print(res)

# k - 75% (prediction is good)
