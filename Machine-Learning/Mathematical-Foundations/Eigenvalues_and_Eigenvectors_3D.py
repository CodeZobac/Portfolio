import numpy as np

X = np.array([[25, 2, 9], [5, 26, -5], [3, 7, -1.]])
Value, Vector = np.linalg.eig(X)
value1 = Value[0]
vector1 = Vector[:, 0]
value2 = Value[1]
vector2 = Vector[:, 1]
value3 = Value[2]
vector3= Vector[:, 2]
Verify1 = np.dot(X, vector1)
verify1 = value1 * vector1
Verify2 = np.dot(X, vector2)
verify2 = vector2 * value2
Verify3 = np.dot(X, vector3)
verify3 = vector3 * value3
print(Verify1)
print(verify1)
print(Verify2)
print(verify2)
print(Verify3)
print(verify3)



