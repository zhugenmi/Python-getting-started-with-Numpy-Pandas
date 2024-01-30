import pandas as pd

df=pd.read_csv("../data/covid19_day_wise.csv")
print(df.head())

# 获取 2020 年 2 月 3 日的所有数据
print(
    "日期->索引转换：\n",
    df[df["Date"]=="2020-02-03"]
)
print("日期列表摘取：",df["Date"][:4])

# 2020 年 1 月 24 日之前的累积确诊病例有多少个？
confirmed0124=df.loc[df["Date"]=="2020-01-24","Confirmed"]
print("截止 1 月 24 日的累积确诊数：", confirmed0124.values) # confirmed0124还包括索引信息

# 2020 年 7 月 23 日的新增死亡数是多少？
new_death=df.loc[df["Date"]=="2020-07-23","New deaths"]
print("截止 7 月 23 日的新增死亡数：",new_death.values)

# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
date=pd.to_datetime(df["Date"])
date_range=(date>="2020-01-25")&(date<="2020-07-22")
new_cases=df.loc[date_range,"New cases"]
print("共新增：",new_cases.sum())

# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
not_zero_mask = df["New recovered"] != 0 # 把 New recovered 为零的数都剔除掉
ratio = df.loc[not_zero_mask, "New cases"] / df.loc[not_zero_mask, "New recovered"]
# 平均比例, 标准差
ratio_mean = ratio.mean()
ratio_std = ratio.std()
print("平均比例：", ratio_mean, "；标准差：", ratio_std)

# 画图展示新增确诊的变化曲线
df["New cases"].plot()

# 画图展示死亡率的变化曲线
df["Deaths / 100 Cases"].plot()