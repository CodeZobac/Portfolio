import torch

A = torch.tensor([[25, 2, -5], [3, -2, 1], [5, 7, 4.]])
value, vector = torch.linalg.eig(A)
Vector = vector.float()
Value = value.float()
Vector1 = Vector[:, 0]
Value1 = Value[0]
Av = torch.matmul(A, Vector1)
Av1 = Value1 * Vector1
print(Av)
print(Av1)
Vector2 = Vector[:, 1]
Value2 = Value[1]
Av2 = torch.matmul(A, Vector2)
AV2 = Value2 * Vector2
print(Av2)
print(AV2)
Vector3 = Vector[:, 2]
Value3 = Value[2]
Av3 = torch.matmul(A, Vector3)
AV3 = Vector3 * Value3
print(Av3)
print(AV3)