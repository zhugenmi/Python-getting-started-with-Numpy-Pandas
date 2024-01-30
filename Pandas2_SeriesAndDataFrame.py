import pandas as pd
import numpy as np

l=[4,5,6]
s=pd.Series(l)
print("list: ",l)
print("series: ",s)

# 自定义索引
s=pd.Series(l,index=["a","b","c"])
print(s)

# 只要有索引形式的结构，就可以写成Series
print(pd.Series({"a":7,"b":8,"c":9}))

# 也可以通过numpy创建Series
print(
    pd.Series(np.random.rand(3),index=["a","b","c"])
)

# Series回退到numpy或者list
print("array: ",s.to_numpy())
print("list: ",s.to_list())

df=pd.DataFrame([
    [1,2],
    [3,4]
])
print(df)

# 第 0 行，第 1 列
# 或 第一个维度中的第 0 号，第二个维度中的第 1 号
print(df.at[0, 1])  # 2

# 改变索引序号为文字标签信息
df=pd.DataFrame({"col1":[1,3],"col2":[2,4]})
print(df)

# DataFrame中的一个Column就是一条Series
print(df["col1"], "\n")
print("取出来之后的 type：", type(df["col1"]))
df=pd.DataFrame({
    "col1":pd.Series([1,3]),
    "col2":pd.Series([2,4])
})

# 为Series和DataFrame构建索引
s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
df = pd.DataFrame({"col1": [1,3], "col2": [2, 4]}, index=["a", "b"])
print(s, "\n")
print(df)

# 获取索引和特征
print(df.index, "\n")
print(df.columns)

# 比如还可以处理json形式的数据
my_json_data = [
  {"age": 12, "height": 111},
  {"age": 13, "height": 123}
]
pd.DataFrame(my_json_data, index=["jack", "rose"])

# DataFrame转化成Numpy
df.to_numpy()