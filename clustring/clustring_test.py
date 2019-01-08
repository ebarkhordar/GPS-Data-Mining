import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import deepcopy
from numpy import array

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
data = pd.read_csv("Porto_taxi_data_test_partial_trajectories.csv", error_bad_lines=False)
data = data.head()
print(data.head())
poly_lines = data['POLYLINE']
XX = None
for i in range(0, len(poly_lines)):
    polyLine = pd.io.json.loads(poly_lines.loc[i])
    if i == 0:
        XX = array(polyLine)
    else:
        XX = np.vstack((array(polyLine), XX))
# print(X)
f1 = [item[0] for item in XX]
f1 = array(f1)
print(type(f1))
f2 = [item[1] for item in XX]
f2 = array(f2)
print(type(f2))

X = np.array(list(zip(f1, f2)))

plt.scatter(f1, f2, c='black', s=6)
plt.show()
# Number of clusters
k = 2
# X coordinates of random centroids
C_x = np.random.randint(0, np.max(X) - 20, size=k)
# Y coordinates of random centroids
C_y = np.random.randint(0, np.max(X) - 20, size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print(C)

# Plotting along with the Centroids
plt.scatter(f1, f2, c='#050505', s=7)
plt.scatter(C_x, C_y, marker='*', s=200, c='g')


# Euclidean Distance Caculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)


# To store the value of centroids when it updates
C_old = np.zeros(C.shape)
# Cluster Lables(0, 1, 2)
clusters = np.zeros(len(X))
# Error func. - Distance between new centroids and old centroids
error = dist(C, C_old, None)
# Loop will run till the error becomes zero
while error != 0:
    # Assigning each value to its closest cluster
    for i in range(len(X)):
        distances = dist(X[i], C)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    # Storing the old centroid values
    C_old = deepcopy(C)
    # Finding the new centroids by taking the average value
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old, None)
colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
    points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')
plt.show()
