import torch
#Prova que P=VΛV^−1 :
P = torch.tensor([[25, 2, -5], [3, -2, 1], [5, 7, 4.]])
lambdas, V = torch.linalg.eig(P)
Vinv = torch.linalg.inv(V)
lambda1 = torch.diag(lambdas)
p = torch.matmul(V, torch.matmul(lambda1, Vinv))
print(p)
#Prova que S=QΛQ^T(Only simmetric matrices)
S = torch.tensor([[25, 2, -5], [2, -2, 1], [-5, 1, 4.]])
lambdas1, V = torch.linalg.eig(S)
lambda2 = torch.diag(lambdas1)
s = torch.matmul(V, torch.matmul(lambda2, V.T))
print(s)
