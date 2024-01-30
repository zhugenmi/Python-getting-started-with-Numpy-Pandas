import pandas as pd
import numpy as np

data = np.arange(-12, 12).reshape((6, 4))
df = pd.DataFrame(
    data,
    index=list("abcdef"),
    columns=list("ABCD"))

# 筛选 A列进行乘以0的运算
df["A"] *= 0

# 记住iloc找的是index，loc 找的是标签。
df.loc["a", "A"] = 100
df.iloc[1, 0] = 200

# a行乘以2
df.loc["a", :] = df.loc["a", :] * 2

# 将df["A"]中等于0的数赋值为-1
df["A"][df["A"] == 0] = -1

df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
# 对df做全量的平方根计算
np.sqrt(df)

# 使用apply
df.apply(np.sqrt)

print(df)


# 对于复杂一点的情况，apply更有用
def func(x):
    return x[0] * 2, x[1] * -1

# 对列应用函数func
tt=df.apply(func, axis=1, result_type='expand')
tt=df.apply(func, axis=1, result_type='broadcast')
print("tt: ",tt)


# 只改一列
def func(x):
    return x["A"] * 4

df.apply(func, axis=1)

# 对row操作
def func(r):
    return r[2] * 4

last_row = df.apply(func, axis=0)
print("last_row:\n", last_row)

df.iloc[2, :] = last_row
print("\ndf:\n", df)
