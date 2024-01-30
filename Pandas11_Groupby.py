import numpy as np
import pandas as pd

df = pd.DataFrame(
    [
        ("小红", "哈利波特", 80),
        ("小明", "蜘蛛侠", 72),
        ("小红", "雷神", 83),
        ("小红", "蜘蛛侠", 45),
        ("小明", "超人", 57),
    ],
    columns=["人", "人物", "评价"],
)
grouped = df.groupby("人")
print(grouped.groups) # 保存的是不同人的row index
print(df.iloc[grouped.groups["小明"]])
# 或者直接在 grouped 的基础上，get_group()。
grouped.get_group("小明")

# 返回每个组的第一个数据
grouped.first()
# 返回每个组的最后一个数据
grouped.last()
# 对每个组里面的数据进行操作
grouped.sum()
# 聚合计算
grouped = df.groupby("人")
grouped.aggregate(np.sum)
# 多种计算操作
grouped["评价"].agg([np.sum, np.mean, np.std])
# 重新命名描述
grouped["评价"].agg(
    [np.sum, np.mean, np.std]
).rename(columns={
    "sum": "合",
    "mean": "均值",
    "std": "标准差"
})

# 循环操作
for name, group in grouped:
    print("name:", name)
    print(group)

# 多从分组
df = pd.DataFrame(
    [
        ("小红", "哈利波特", 80),
        ("小明", "蜘蛛侠", 72),
        ("小红", "雷神", 83),
        ("小红", "雷神", 90),
        ("小红", "蜘蛛侠", 45),
        ("小明", "超人", 57),
    ],
    columns=["人", "人物", "评价"],
)
# 按照人和人物进行分组，并查看小红和雷神的评价
df.groupby(["人", "人物"]).get_group(("小红", "雷神"))