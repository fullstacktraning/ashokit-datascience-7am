import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
X = np.array([[1,1],[1,2],[2,1],[8,8],[8,9],[50,50]])
model = DBSCAN(eps=2,min_samples=3)
labels = model.fit_predict(X)
print(labels)

print("Cluster Labels:", labels)

# Step 4: Scatter Plot
plt.scatter(X[:,0], X[:,1], c=labels)

# Optional: Label points
for i, txt in enumerate(range(len(X))):
    plt.annotate(txt, (X[i,0], X[i,1]))

plt.title("Agglomerative Clustering")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()