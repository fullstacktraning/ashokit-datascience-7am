from sklearn.tree import DecisionTreeClassifier

X = [[2],[5],[6],[1]]

y = ["fail","pass","pass","fail"]

model = DecisionTreeClassifier()

model.fit(X,y)

res = model.predict([[35]])

print(res)