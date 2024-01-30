import pandas as pd
import numpy as np

data = np.array([
    [1.39, 1.77, None],
    [0.34, 1.91, -0.05],
    [0.34, 1.47, 1.22],
    [None, 0.27, -0.61]
])
df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"])

# 获取数据的基础信息
print(df.describe())
# 如果是纯数据，还能看到统计学的信息
df1 = pd.DataFrame(np.random.random((4,3)), columns=["c0", "c1", "c2"])
print(df1)
print("\ndescribe:\n", df1.describe())

# 均值中位数
print(df.mean())
# 第0个维度求均值
print(df.mean(axis=0))
# 当 skipna=False 的时候， Pandas 只要遇到了 None 或者 NaN，就不计算这列、行的数据了。所以下面你会看到，它只返回了一个 column 的结果。
# print(df.mean(axis=0,skipna=False))

# 中位数
# 最后一个为高收入人
s = pd.Series([1000, 2000, 4000, 100000])
print("mean():", s.mean())   # 拉高平均收入，拉高仇恨
print("median():", s.median())  # 比较合理

# 累加累乘
print("sum():\n", df.sum())
print("\nsum(axis=0):\n", df.sum(axis=0))
print("\nsum(axis=1):\n", df.sum(axis=1))

print("prod():\n", df.prod())
print("\nprod(axis=0):\n", df.prod(axis=0))
print("\nprod(axis=1):\n", df.prod(axis=1))

# 最大最小
print(df.max().max())
print(df.values.ravel().max())  # 用 Numpy 的方式运算

# 判空
print("\nisnull():\n", df.isnull())  # True 就是空
print("\nnotnull()\n", df.notnull())  # False 为空

print("默认：\n", df.dropna())  # 默认按 axis=0
print("\naxis=1:\n", df.dropna(axis=1))  # 可以换一个 axis drop

# 对空值进行填充
df.fillna(111)  # 填充 111

# 根据不同特征进行差异化填充数据
values = {"A": 0, "B": 1, "C": 2, "D": 3}
df.fillna(value=values)

# 甚至可以用另一个大小相对应的df来填充
df2 = pd.DataFrame(np.arange(16).reshape((4,4)), columns=list("ABCD"))
print("df2:\n", df2)
print("\nfillna(df2):\n", df.fillna(df2))

# 找到最大最小值的索引
print("\nidxmax():\n", df.idxmax())
print("\nidxmax(skipna=False):\n", df.idxmax(skipna=False))
print("\nidxmin():\n", df.idxmin())