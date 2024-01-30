import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 散点图 Scatter
n = 1024    # data size
df = pd.DataFrame({
    "x": np.random.normal(0, 1, n),
    "y": np.random.normal(0, 1, n),
})
color = np.arctan2(df["y"], df["x"])
# 散点图 c：每个数据点的颜色值 s：画点的大小 alpha：不透明度 cmap：colormap
df.plot.scatter(x="x", y="y", c=color, s=60, alpha=.5, cmap="rainbow")

# 折线图 Plot
n = 20    # data size
x = np.linspace(-1, 1, n)
y = x * 2 + 0.4 + np.random.normal(0, 0.3, n)
df = pd.DataFrame({
    "x": x,
    "y": y,
})
df.plot(x="x", y="y", alpha=.5, c="r")

# 多条线的情况
y1 = x * -1 - 0.1 + np.random.normal(0, 0.3, n)
df=pd.DataFrame({
    "x":x,
    "y1":y,
    "y2":y1
})
df.plot(x="x",y=["y1","y2"],alpha=.5)

# 条形图 Bar
df = pd.DataFrame(np.random.rand(5, 3), columns=["a", "b", "c"])
df.plot.bar()
# 放在一起看占比
df.plot.bar(stacked=True)
# 水平柱状图
df.plot.barh()

# 分布图 Hist
df = pd.DataFrame({"a": np.random.randn(1000)})
df.plot.hist()
# 多个分布重合在一起
df = pd.DataFrame(
    {
        "a": np.random.randn(1000) + 1,
        "b": np.random.randn(1000),
        "c": np.random.randn(1000) - 4,
    }
)

df.plot.hist(alpha=0.5, bins=30)

# 饼图Pie
df = pd.DataFrame(
    {"boss": np.random.rand(4)},
    index=["meeting", "supervise", "teaching", "team building"],
)
df.plot.pie(y="boss", figsize=(7,7))
# 分开画饼，legend 是用来确定要不要输出图例
df = pd.DataFrame(
    {
        "bigBoss": np.random.rand(4),
        "smallBoss": np.random.rand(4),
    },
    index=["meeting", "supervise", "teaching", "team building"],
)
df.plot.pie(subplots=True, figsize=(9,9), legend=False)

# 画面积Area
df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=["a", "b", "c", "d"]
)
df.plot.area()
df.plot.area(stacked=False)

plt.show()
