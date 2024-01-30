import numpy as np

# 一、单个选取
a = np.array([1, 2, 3])
print("a[0]:", a[0])
print("a[[0,1]]:\n", a[[0,1]])
print("a[[1,1,0]]:\n", a[[1,1,0]])

b = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
])

# 选第 2 行所有数
print("b[1]:\n", b[1])

# 选第 2 行，第 1 列的数
print("b[1,0]:\n", b[1,0])

# 二、切片划分
a = np.array([1, 2, 3])
print("a[0:2]：\n", a[0:2])
print("a[1:]：\n", a[1:])
print("a[-2:]：\n", a[-2:])
# 多维切片划分
b = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
])

print("b[:2]:\n", b[:2])
print("b[:2, :3]:\n", b[:2, :3])
print("b[1:3, -2:]:\n", b[1:3, -2:])

# 三、条件筛选
a = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
])

print(a[a>7]) # 选取 a 数据中，大于 7 的数据

# 拆解以上表达式
condition = (a > 7) & (a != 10) # condition 是一种 True/False
print(a[condition])

# 想要按条件选择、替换数据的时候，就需要强大的的np.where()
condition = a > 7
print(np.where(condition, -1, a)) # 满足condition的将值替换为-1；不满足的还是a（也可替换为其他值）

