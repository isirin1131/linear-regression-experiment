import numpy as np
import torch
from torch.utils import data
from torch import nn

# 用库真的很爽，代码整整少了一半的行数

true_w = torch.tensor([3, -1.2])
true_b = 2.1
def datamaker(source_w, source_b, want_num):
    # 这里就是直接按照我们的假设来生成数据
    _data_X = torch.normal(0, 1, (want_num, len(source_w)))
    _data_y = torch.mv(_data_X, source_w) + source_b
    _data_y += torch.normal(0, 0.01, _data_y.shape)
    return _data_X, _data_y

data_X, data_y = datamaker(true_w, true_b, 100)


# iter 只需三行，真的是太棒了
batchsize = 10
dataset = data.TensorDataset(*(data_X, data_y))
dataiter = data.DataLoader(dataset=dataset, batch_size=batchsize, shuffle=True)

# print(next(iter(dataiter)))

# 模型初始化
net = nn.Sequential(nn.Linear(2, 1, bias=True))
net[0].weight.data.normal_(0, 1)
net[0].bias.data.fill_(0)

# loss 和训练方法
loss = nn.MSELoss()
trainer = torch.optim.SGD(net[0].parameters(), lr=0.1)


train_epochs = 5
for epoch in range(train_epochs) :
    for batch_X, batch_y in dataiter :
        batch_loss = loss(net(batch_X)[:,0], batch_y)
        # print(net(batch_X)[:,0]) # 这个不用管太多，无用的小细节罢了
        trainer.zero_grad()
        batch_loss.backward()
        trainer.step()
    epoch_loss = loss(net(data_X)[:,0], data_y)
    print(f'epoch {epoch + 1}, loss {epoch_loss:f}')

print("model_w : ", net[0].weight.data, ", model_b : ", net[0].bias.data)