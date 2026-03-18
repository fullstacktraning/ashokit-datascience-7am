from sklearn import svm
# read data from Excel Sheet
X = [[1],[2],[4],[5],[6]]
y = [0,0,1,1,1]
model = svm.SVC(kernel="linear")
model.fit(X,y)
print(model.coef_)
print(model.intercept_)
# read input from Swagger 
print(model.predict([[1.5]]))