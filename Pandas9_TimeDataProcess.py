import numpy as np
import pandas as pd
import datetime

df = pd.DataFrame({
    "time": ["2022/03/12", "2022/03/13", "2022/03/14"],
    "value": [1,2,3]
})
print(df)
print("\n\ntime:\n",df["time"])

# 把time套上时间序列标识
pd.to_datetime(df["time"])
print("\n\ntime:\n",df["time"])

# 按照指定规则解析时间
pd.to_datetime(
    [
        "1@21@2022%%11|11|32",
        "12@01@2022%%44|02|2",
        "4@01@2022%%14|22|2"
    ],
    format="%m@%d@%Y%%%%%S|%H|%M"
)
# %m 月
# %d 日
# %Y 年的全称
# %% 比配一个 %
# %S 秒
# %H 时
# %M 分

# 批量生成时间戳
start = datetime.datetime(2022, 3, 12)
end = datetime.datetime(2022, 3, 18)
index = pd.date_range(start, end)
print(index)

print(
    "range(1,10,2)\n",
    list(range(1,10,2)) # 步长为2
)
print(
    "\n\npd.date_range()\n",
    pd.date_range(start,end,freq="48h") # 时间间隔48h
)

print(
    "np.linspace(-1, 1, 5)\n",
    np.linspace(-1, 1, 5) # 区间内均匀分割
)
print(
    "\n\npd.date_range(start, end, periods=5)\n",
    pd.date_range(start, end, periods=5) # 对日期分割
)

# 选取时间
start = datetime.datetime(2022, 3, 1)
end = datetime.datetime(2022, 5, 3)

rng = pd.date_range(start, end)
ts = pd.Series(np.random.randn(len(rng)), index=rng)

ts.index

ts.plot()
ts[1:8].plot() # 分片，展示前一周的数据
ts["2022-03"].plot() # 只看3月的数据
# 通过时间本身分片
t1 = datetime.datetime(2022, 3, 12)
t2 = datetime.datetime(2022, 3, 18)
ts[t1: t2].plot()
# equal to ts["2022-03-12": "2022-03-18"].plot()

# 时间运算
rng = pd.date_range("2022-01-01", "2022-01-07")
rng + pd.Timedelta(weeks=1)
# Timedelta 是一种用于时间加减的时间单位，我们可以个任何一个 Timestamp 加减一个时间。而且 Timedelta 还可以乘除。
rng+2*pd.Timedelta(days=3)

rng = pd.date_range("2022-01-08", "2022-01-11")
print(rng.dayofyear)
print(rng.dayofweek)

rng.strftime("%m/%d/%Y")  # 按规则输出日期形式

# 时区设置
s = pd.to_datetime(
    ["2022/03/12 22:11", "2022/03/12 12:11", "2022/03/12 2:11"]
)
s_us = s.tz_localize("America/New_York")
s_cn = s_us.tz_convert("Asia/Shanghai")

# 生成时间时带上时区
rng = pd.date_range(
    "2022-01-08", "2022-01-11",
    tz="America/New_York")