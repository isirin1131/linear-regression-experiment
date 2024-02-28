'''
书上的实验，为了表明我们用的库都是很快的
不像 C++、C，那些语言自己写 for 循环可能更快
python 的 for 循环很慢
所以不如老老实实用计算库
'''

import time
import torch

class Timer:
    """记录多次运行时间"""
    def __init__(self):
        self.times = []
        self.start()

    def start(self):
        """启动计时器"""
        self.tik = time.time()

    def stop(self):
        """停止计时器并将时间记录在列表中"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self):
        """返回平均时间"""
        return sum(self.times) / len(self.times)

    def sum(self):
        """返回时间总和"""
        return sum(self.times)

    def cumsum(self):
        """返回累计时间"""
        return np.array(self.times).cumsum().tolist()


'''
贴个实验结果（n = 1000000）
4.38200 sec （自己循环）
0.00092 sec （用库）

n 调小下面就直接小到五位小数无法表示了，所以我改成了保留七位，
但发现依然是 n = 1000000 的时候用库计算才能统计出数据。

CPU : intel i7-12650H

'''
n = 1000000
a = torch.ones(n)
b = torch.ones(n)
c = torch.zeros(n)
timer = Timer()


timer.start()
for i in range(n):
    c[i] = a[i] + b[i]
print(f'{timer.stop():.7f} sec')

timer.start()
c = a + b
print(f'{timer.stop():.7f} sec')