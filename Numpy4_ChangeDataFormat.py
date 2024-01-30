import numpy as np

# 一、改变形态
a = np.array([1,2,3,4,5,6])
# 添加维度法一
a_2d = a[np.newaxis, :]
print(a.shape, a_2d.shape)
# 添加维度法二
a_none = a[:, None]
a_expand = np.expand_dims(a, axis=1) # 变为6行一列
print(a_expand)
print(a_none.shape, a_expand.shape)

# 减少维度
a_squeeze = np.squeeze(a_expand)
print(a_squeeze)
a_squeeze_axis = a_expand.squeeze(axis=1)
print(a_squeeze.shape)
print(a_squeeze_axis.shape)

a1 = a.reshape([2, 3])
a2 = a.reshape([3,1,2])
print("a1 shape:", a1.shape)
print(a1)
print("a2 shape:", a2.shape)
print(a2)

# 矩阵转置两种方法
a = np.array([1,2,3,4,5,6]).reshape([2, 3])
aT1 = a.T
aT2 = np.transpose(a)

print(aT1)
print(aT2)

# 二、合并
feature_a = np.array([1,2,3,4,5,6])
feature_b = np.array([11,22,33,44,55,66])
# 列合并
c_stack = np.column_stack([feature_a, feature_b])
print(c_stack)
# 行合并
c_stack=np.row_stack([feature_a,feature_b])
print(c_stack)

# 更好的合并方式
a = np.array([
[1,2],
[3,4]
])
b = np.array([
[5,6],
[7,8]
])

print(np.concatenate([a, b], axis=0))
print(np.concatenate([a, b], axis=1))

# 三、拆解
a = np.array(
[[ 1, 11, 2, 22],
 [ 3, 33, 4, 44],
 [ 5, 55, 6, 66],
 [ 7, 77, 8, 88]]
)
# 在 indices_or_sections 后填入数字，就是要整分的段数， 而如果接着的是一个列表，那就按照列表中的 index 来取区间。
print(np.split(a, indices_or_sections=2, axis=0))  # 分成两段
print(np.split(a, indices_or_sections=[2,3], axis=1))  # 在第二维度，分片成 [:2]，[2:3]，[3:]