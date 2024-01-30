import numpy as np
import matplotlib.pyplot as plt

with open("../data/covid19_day_wise.csv","r",encoding="utf-8") as f:
    data=f.readlines()

covid={
    "date":[],
    "data":[],
    "header":[h for h in data[0].strip().split(",")[1:]]
}
for row in data[1:]:
    split_row=row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])

print("日期列表摘取：",covid["date"][:4])

# 获取 2020 年 2 月 3 日的所有数据
date_idx=covid["date"].index("2020-02-03")
print("日期->索引转换：",date_idx)
data=np.array(covid["data"])
for header,number in zip(covid["header"],data[date_idx]):
    print(header,":",number)

# 2020 年 1 月 24 日之前的累积确诊病例有多少个？
row_idx=covid["date"].index("2020-01-24") # 获取日期索引
column_idx=covid["header"].index("Confirmed") # 获取标题的索引
confirmed0124=data[row_idx,column_idx]
print("截止2020年 1 月 24 日的累积确诊数：", confirmed0124)

# 2020 年 7 月 23 日的新增死亡数是多少？
row_idx=covid["date"].index("2020-07-23")
column_idx=covid["header"].index("New deaths")
result=data[row_idx,column_idx]
print("截止2020年 7 月 23 日的新增死亡数：", result)

# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
row1_idx = covid["date"].index("2020-01-25")
row2_idx = covid["date"].index("2020-07-22")
new_cases_idx = covid["header"].index("New cases")
# 注意要 row1_idx+1 得到从 01-25 这一天的新增
# row2_idx+1 来包含 7 月 22 的结果
new_cases = data[row1_idx+1: row2_idx+1, new_cases_idx]
overall = new_cases.sum()
print("共新增：", overall)

# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
new_cases_idx=covid["header"].index("New cases")
new_recovered_idx=covid["header"].index("New recovered")
# 比例
not_zero_mask = data[:, new_recovered_idx] != 0 # 剔除new_recovered 为零的数
ratio=data[not_zero_mask,new_cases_idx] / data[not_zero_mask,new_recovered_idx]
print("比例样本：",ratio[:5])
ratio_mean=ratio.mean() # 平均比例
ratio_std=ratio.std() # 标准差
print("平均比例：",ratio_mean,"；标准差：",ratio_std)

def draw_line(x):
    plt.plot(x)
    plt.show()

# 画图展示新增确诊的变化曲线
new_cases_idx = covid["header"].index("New cases")
draw_line(data[:, new_cases_idx])

# 画图展示死亡率的变化曲线
death_ratio_idx = covid["header"].index("Deaths / 100 Cases")
draw_line(data[:, death_ratio_idx])

