import torch
import numpy as np
A = torch.tensor([[-1, 2], [3, -2.], [5, 7]])
b = torch.tensor([[0, 0]])
U, d, Vt = torch.linalg.svd(A)
D = torch.diag(d)
dinv = torch.linalg.inv(D)
dplus = torch.tensor([[0.1154, 0, 0], [0, 0.2436, 0]])
Aplus = torch.matmul(Vt.T, torch.matmul(dplus, U.T))
aplus = torch.pinverse(A)
print(Aplus), print(aplus)
A = torch.tensor([[25, 2], [5, 4]])
b = A.T
print(b)
