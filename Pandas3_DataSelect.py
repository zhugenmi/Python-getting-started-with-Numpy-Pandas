import pandas as pd
import numpy as np

data=np.arange(-12,12).reshape((6,4))
df=pd.DataFrame(
    data,
    index=list("abcdef"),
    columns=list("ABCD")
)
print(df)

# 提取特征
print(df["B"])

# 提取多列特征
print("numpy: \n",data[:,[2,1]])
print("\n df: \n",df[["C","B"]])

# 筛选片段
print(data[2:3,1:3])  # 似乎等同于下面，但是pandas包括了“d”和“D”列
print(df.loc["c":"d","B":"D"])

# 单个提取
print("numpy:\n",data[[3,1],:])
print("\ndf:\n",df.loc[["d","b"],:])

# 将序号索引转换为.loc的标签索引
row_labels = df.index[2:4]
print("row_labels:\n", row_labels)
print("\ndf:\n", df.loc[row_labels, ["A", "C"]])

col_labels = df.columns[[0, 3]]
print("col_labels:\n", col_labels)
print("\ndf:\n", df.loc[row_labels, col_labels])

# A B两个特征的前两个数据
col_index = df.columns.get_indexer(["A", "B"])
print("col_index:\n", col_index)
print("\ndf:\n", df.iloc[:2, col_index])

# 条件过滤筛选
# 选在 A Column 中小于 0 的那些数据
df[df["A"]<0]

# 选在第一行数据不小于 -10 的数据 .iloc数字索引
print(df.loc[:,~(df.iloc[0]<-10)])

list_data = list(range(-4, 4))
s = pd.Series(
  list_data,
  index=list("abcdefgh"))

# 按标签筛选数据.loc
print(s.loc[["a", "g", "c"]], "\n")
print(s.loc["c": "f"])

# 按 index 筛选数据 .iloc
print(s.iloc[[3, 1, 5]], "\n")
print(s.iloc[2: 4])

# iloc 和 loc 互相混用
print(s.iloc[s.index.get_indexer(["c", "d"])], "\n")
print(s.loc[s.index[[3,2]]])

# 按条件过滤筛选
print(s.loc[s < 3], "\n")
print(s.loc[(s < 0) & (s > -2)], "\n")
print(s.loc[(s < 0) | (s > 2)], "\n")