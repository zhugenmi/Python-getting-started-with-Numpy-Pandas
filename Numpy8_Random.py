import random
import numpy as np

# 自带的random
print(random.random())
print(random.randint(1, 10))

# 随机生成 [0, 1) 之间的二维数据
dim1, dim2 = 3, 2
print(np.random.rand(dim1, dim2)) # 你还能继续添加 dim3 或更多

print(np.random.randn(dim1, dim2)) # 按照标准正态分布生成

print(np.random.randint(low=-3, high=6, size=10)) # 生成随机整数

data = np.array([2,1,3,4,6])
print("选一个：", np.random.choice(data))
print("选多个：", np.random.choice(data, size=3))
print("不重复地选多个(不放回)：", np.random.choice(data, size=3, replace=False))
print("带权重地选择：", np.random.choice(data, size=10, p=[0,0,0,0.2,0.8]))

data_copy = np.copy(data)
np.random.shuffle(data) # 洗牌
print("源数据：", data_copy)
print("shuffled:", data)

print("直接出乱序序列：", np.random.permutation(10))
data = np.arange(12).reshape([6,2])
print("多维数据在第一维度上乱序：", np.random.permutation(data))

# (均值，方差，size)
print("正态分布：", np.random.normal(1, 0.2, 10))

# (最低，最高，size)
print("均匀分布：", np.random.uniform(-1, 1, 10))

# seed(1) 代表的就是 1 号随机序列 同一个种子（数字）产生的随机序列就会一样。
np.random.seed(1)
print(np.random.randint(2, 10, size=3))
print(np.random.randint(2, 10, size=3))

np.random.seed(2)
print(np.random.randint(2, 10, size=3))
np.random.seed(2)
print(np.random.randint(2, 10, size=3))