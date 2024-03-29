高斯/正态分布函数：$\sigma$ 为随机变量 $x$ 的标准差，它大峰平，它小峰尖；$\mu$ 为随机变量 $x$ 的均值，也是图像的对称轴。（$\mu=0,\sigma=1$ 的正态分布函数叫标准正态分布函数）

在线性回归的问题中，如果我们假设训练集中的样本真的是出于某个线性模型，它们只能被线性模型拟合而不能被完全概括的原因是有采样噪声，而且采样噪声为独立同分布的高斯分布下的采样，那么就可以用极大似然估计法去估计那个最可能得出这些样本的线性模型，在这种假设下，我们最终会发现极大似然估计等价于最小二乘估计，也等价于最小化我们那个经典的损失函数。

在采样噪声为伯努利分布的假设下，极大似然估计的结论是逻辑回归
在采样噪声为多项分布（multinomial）的假设下，极大似然估计的结论是 softmax 回归

在极大似然估计的实践中，我们经常用 $\log$ 函数来化掉连乘号 $\prod$（有时也可以化掉指数）