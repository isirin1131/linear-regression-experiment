import matplotlib.pyplot as plt
import numpy as np
from d2l import torch as d2l

def f(x):
    return x * x + 2

plt.title("just a stupid title")
plt.xlim(-10,10)
plt.xlabel("X")
plt.ylim(0, 20)
plt.ylabel("Y")

X = np.arange(-10, 10, 0.01)
plt.plot(X, f(X))
plt.plot(X, 2 * X + 1)

plt.show()