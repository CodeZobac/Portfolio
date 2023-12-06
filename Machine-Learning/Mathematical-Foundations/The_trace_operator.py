import torch
A = torch.tensor([[-1, 2], [3, -2], [5, 7.]])
at = torch.trace(A)
# prova frobenius norm
AAt = torch.matmul(A, A.T)
aat = torch.trace(AAt)
Af = aat**(1/2)
AF = torch.norm(A)
print(Af, AF)
