import math
import torch
from torch.distributions import multinomial
from torch.distributions import binomial
from torch.distributions import bernoulli
from torch.distributions import normal
import matplotlib.pyplot as plt
import numpy as np

#          -----  伯努利分布  -----
x = bernoulli.Bernoulli(torch.tensor([0.3])).sample((1000,))
print(x.sum()) # 0.3 概率采样为 1，0.7 概率采样为 0，采样 1000 次

#          -----  二项分布，其实就是多次伯努利采样得到的分布 -----
y = binomial.Binomial(4, 0.3)
yy = y.sample((1000,))
print(torch.sum(yy == 0).item(), torch.sum(yy == 1).item(), torch.sum(yy == 2).item(),
      torch.sum(yy == 3).item(), torch.sum(yy == 4).item())

#          -----  多项分布，就是把伯努利的硬币变成了多面骰子 -----
z = multinomial.Multinomial(1000, torch.tensor([0.2, 0.3, 0.5])).sample()
print(z)

#    标准正态分布，由于在连续域采样得到的直方图不好转成概率密度函数，所以就把标准正态函数变形了一下下，
#    主要是看采样直方图的形状，不必太严格
Gauss = normal.Normal(torch.tensor(0.), torch.tensor(1.)).sample([20000])
plt.title("just a stupid title")
plt.xlim(-10,10)
plt.xlabel("X")
plt.ylim(0, 400)
plt.ylabel("Y")

gauss = np.array(Gauss)
#Y = np.zeros(100)
plt.hist(gauss, bins=1000)

def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu)**2) * 200

X = np.arange(-10, 10, 0.01)
plt.plot(X, normal(X, 0, 1))
plt.show()