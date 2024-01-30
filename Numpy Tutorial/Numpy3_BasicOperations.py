import numpy as np

# 一、加减乘除
a = np.array([150, 166, 183, 170])
print(list(map(lambda x: x+3, a))) # 等同于
print(a + 3)

# 矩阵点乘运算
a = np.array([
[1, 2],
[3, 4]
])
b = np.array([
[5, 6],
[7, 8]
])

print(a.dot(b)) # 等同于
print(np.dot(a, b))
# np.outer() 矩阵外积  np.inner() 矩阵内积  可以理解np.dot(a, b）= np.inner(a, b.T)

# 二、数据统计分析
a = np.array([150, 166, 183, 170])
print("最大：", np.max(a))
print("最小：", a.min())
print("总和：", a.sum())
print("累乘：", a.prod())
print("总数：", a.size)

a = np.array([0, 1, 2, 3])
print("非零总数：", np.count_nonzero(a))

month_salary = [1.2, 20, 0.5, 0.3, 2.1]
print("平均工资：", np.mean(month_salary))
print("工资中位数：", np.median(month_salary))

# standard deviation 标准差，用来描述正态分布。 这个在机器学习中，特别是深度神经网络中也非常重要，特别用于权重的生成原则。
month_salary = [1.2, 20, 0.5, 0.3, 2.1]
print("标准差：", np.std(month_salary))

# 三、特殊运算符号
a = np.array([150, 166, 183, 170])
name = ["小米", "OPPO", "Huawei", "诺基亚"]
high_idx = np.argmax(a) # 获得最大值的下标
low_idx = np.argmin(a)
print("{} 最高".format(name[high_idx]))
print("{} 最矮".format(name[low_idx]))

a = np.array([150.1, 166.4, 183.7, 170.8])
print("ceil:", np.ceil(a)) # 向上取整
print("floor:", np.floor(a)) # 向下取整

# 用 np.clip() 来做上下界限的值截取。
a = np.array([150.1, 166.4, 183.7, 170.8])
print("clip:", a.clip(160, 180))