from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Data
X = np.array([
    [1,2],[2,3],[8,8],[9,9],
    [15,2],[16,3],[20,1],[22,2],[50,1]
])

# Step 2: Model
model = AgglomerativeClustering(n_clusters=4)

# Step 3: Training + Predict
labels = model.fit_predict(X)

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