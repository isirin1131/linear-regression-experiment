#### 什么是线性回归

线性回归，即是用线性模型来做数值-数值预测，用于训练的数据长这样：（$(x_0,x_1,\cdots,x_k), y$），简写成这样：（$\mathbb x, y$）,模型要实现的目的是经过这类型的数据训练后，对于同类型的数据，可以通过 $\mathbb x$ 来估计（或者说预测）$y$。

线性回归的模型长这样：

$$
\hat y = w_0x_0+w_1x_1+\cdots+w_kx_k+b
$$

可以简写成（其实就是向量点积，只不过写成矩阵乘法的形式）：

$$
\hat y = \mathbb{w}^T\mathbb{x}+b
$$

模型的样子也就决定了它就算只能做数值-数值预测，但它发挥比较好的也就这类问题的某些子集。

#### 预备知识：向量求导

写这节是为了让读者能看懂后面的公式，原书略过了一些细节，对新手比较致命。

首先要先对矩阵求导有个基本印象，这里可以看我写的 [矩阵求导 (isirin1131.github.io)](https://isirin1131.github.io/%E7%9F%A9%E9%98%B5%E6%B1%82%E5%AF%BC.html)。

其次，我们不需要对完整的矩阵求导建立代数系统，而只需要对向量求导建立理论和得出并记住一些基本结果，这对理解线性回归这一节中的公式已经足够了。（其实是我搞不定更高的理论）

**约定：依据分子布局，所有的向量都是列向量**

**向量求导形如：** 对于向量 $\mathbb x$，其长度为 $n$，形如 $\{x_1,x_2,\cdots, x_n\}$，对于向量 $\mathbb y$，也就是 $\mathbb f(\mathbb x)$，其长度为 $m$，形如 $\{f_1(\mathbb x),f_2(\mathbb x),\cdots,f_m(\mathbb x)\}$，我们要求 $\dfrac{\partial}{\partial\mathbb x}\mathbb y$，得到的结果是个 $m\times n$ 的矩阵，并且如果 $\mathbb y\mathbb x^T$ 这个 $m\times n$ 矩阵的第 $(i,j)$ 项是 $f_i(\mathbb x)\mathbb x_j$，那么 $\dfrac{\partial}{\partial\mathbb x}\mathbb y$ 的第 $(i,j)$ 项就是 $\dfrac{\partial}{\partial x_j}f_i(\mathbb x)$。

**几个基础的例子：**

1. $\dfrac{\partial}{\partial\mathbb x}\mathbb a$ 等于 $\mathbb 0$（$\mathbb a$ 是与 $\mathbb x$ 无关的常数向量，$\mathbb 0$ 是全零矩阵），这个很容易推
2. $\dfrac{\partial}{\partial\mathbb x}\mathbb x$ 等于 $\mathbb 1$（$\mathbb 1$ 是一个对角线为 $1$，其余地方为 $0$ 的方阵），这个也比较容易推
3. $\dfrac{\partial}{\partial\mathbb x}\mathbb A\mathbb x$ 等于 $\mathbb A$（$\mathbb A$ 是个列数为 $n$ 的矩阵，行数不做要求），这个稍微有点难，就稍微讲讲，首先 $\mathbb A\mathbb x$ 是个列向量，而且 $\mathbb A\mathbb x$ 的每个分量都是 $\mathbb A$ 的某个行向量与 $\mathbb x$ 的点积，往后就显然了
4. $\dfrac{\partial}{\partial\mathbb x}\mathbb x^T\mathbb A$ 等于 $A^T$，这个跟上一个存在某种对应的关系，读者不需要管，硬推就行了。
5. $\dfrac{\partial}{\partial\mathbb x}\mid \mathbb x\mid^2$ 等于 $2\mathbb x$（$\mid \mathbb x\mid^2$ 意思是向量长度的平方，数值上等于 $\sum_{i=1}^n (x_i)^2$，其实是个标量，但我们也可以把它当成向量处理），这个也比较显然

**这向量求导的这些性质怎么这么像标量求导的那些性质？那既然如此，四则运算求导法则和链式求导法则也存在吗？** 

