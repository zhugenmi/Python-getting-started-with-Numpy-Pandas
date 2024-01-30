import numpy as np

# 脏数据
raw_data = [
["Name", "StudentID", "Age", "AttendClass", "Score"],
["小明", 20131, 10, 1, 67],
["小花", 20132, 11, 1, 88],
["小菜", 20133, None, 1, "98"],
["小七", 20134, 8, 1, 110],
["花菜", 20134, 98, 0, None],
["刘欣", 20136, 12, 0, 12]
]
print(raw_data)

data = np.array(raw_data)
print(data)

# 数据预处理
data_process=[]
for i in range(len(raw_data)):
    if i == 0:
        continue # 跳过首行字符串
    data_process.append(raw_data[i][1:]) # 去掉首列的名字
data=np.array(data_process,dtype=np.float64)
print("data.dtype",data.dtype)
print(data)

# 清洗数据
sid=data[:,0]
unique,counts=np.unique(sid,return_counts=True)
print(counts)

print(unique[counts > 1]) # 查看重复的数据

# 通过查看数据，发现少了一个 20135，可能输错了，修改它
data[4, 0] = 20135
print(data)

is_nan = np.isnan(data[:,1]) # 判断数据是否正常
print("is_nan:", is_nan)
nan_idx = np.argwhere(is_nan)

# 计算有数据的平均年龄，用 ~ 符号可以 True/False 对调
mean_age = data[~np.isnan(data[:,1]), 1].mean()
print("有数据的平均年龄：", mean_age)

# ~ 表示 True/False 对调，& 就是逐个做 Python and 的运算
normal_age_mask = ~np.isnan(data[:,1]) & (data[:,1] < 20)
print("normal_age_mask:", normal_age_mask)

normal_age_mean = data[normal_age_mask, 1].mean()
print("normal_age_mean:", normal_age_mean)

data[~normal_age_mask, 1] = normal_age_mean
print("ages:", data[:, 1])

# 没上课的转成 nan
data[data[:,2] == 0, 3] = np.nan

# 超过 100 分和低于 0 分的都处理一下
data[:, 3] = np.clip(data[:, 3], 0, 100)

print(data[:, 2:])