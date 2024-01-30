import pandas as pd

tuples = [
  # 年级，班级
  ("one", "1"),
  ("one", "1"),
  ("one", "2"),
  ("one", "2"),
  ("two", "1"),
  ("two", "1"),
  ("two", "2"),
  ("two", "2"),
]
index = pd.MultiIndex.from_tuples(
  tuples, names=["grade", "class"])
print(index)

# 构建DataFrame多索引
df1 = pd.DataFrame(
    {"id": [11,12,13,14,15,16,17,18],
    "name":
     ["小米", "小明",     # 一年一班
     "小命", "小勉",      # 一年二班
     "小牛", "小鸟",      # 二年一班
     "小南", "小妮"       # 二年二班
    ]},
    index=index)
print(df1)
print(df1.loc["one"].loc["2"])

# 构建Column多索引
df2 = pd.DataFrame(
    [[11,12,13,14,15,16,17,18],
     ["小米", "小明",      # 一年一班
     "小命", "小勉",      # 一年二班
     "小牛", "小鸟",      # 二年一班
     "小南", "小妮"       # 二年二班
    ]],
    index=["id", "name"],
    columns=index  # 多索引加这
)
print(df2)

# 读取一年级所有学生
print(df2["one"])
# 一年一班
print(df2["one"]["1"])


