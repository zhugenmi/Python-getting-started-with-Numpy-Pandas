import random

import numpy as np

# 创建统一数据
zeros=np.zeros([2,3])
print("zeros: \n",zeros)

ones=np.ones([3,2])
print("ones: \n",ones)

nines=np.full([2,3],9)
print(nines)

data = np.array([
[1,2,3],
[4,5,6]
], dtype=np.int64)

ones = np.ones(data.shape, dtype=data.dtype)
ones_like = np.ones_like(data)

print("ones:", ones.shape, ones.dtype)
print("ones_like:", ones_like.shape, ones_like.dtype)
print("ones value:\n", ones)
print("ones_like value:\n", ones_like)

print(np.zeros_like(data))
print(np.full_like(data, 6))

# 创建规则数据
print("python range:", list(range(5)))
print("numpy arange:", np.arange(5))

# (start, end, step)
print("python range:", list(range(3, 10, 2)))
print("numpy arange:", np.arange(3, 10, 2))

# (start, end, num) 从 start 的值到 end 的值，一共返回这中间 num 个数据点。
print("linspace:", np.linspace(-1, 1, 5))

# 快速创建再添加值
empty = np.empty([2,3]) # 可以看做很快生成一个容器，里面没有具体数值
print("empty before:\n", empty)
data = np.arange(6).reshape([2, 3])
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        empty[i, j] = data[i, j] * random.random()
print("empty after:\n", empty)