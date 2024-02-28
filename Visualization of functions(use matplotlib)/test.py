'''
书上的方法是 d2l 库里自己写的函数，其实也是用的 matplotlib 的 pyplot 这个模块
但是我们不可能一直用 d2l 的库（其实一直用好像也不错）
所以直接原始方法搞一个，虽然效果差
'''

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