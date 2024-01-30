import pandas as pd
import numpy as np

# 从Excel读取数据
df=pd.read_excel("data/体检数据.xlsx",index_col=0) # 使用第一个 column（学号）的数据当做 row 索引
print(df)
df.loc[2,"体重"]=1  # 修改索引为2的体重项
print(df)

# 写入数据
df.to_excel("data/体检数据_修改.xlsx")

# 用python的open打开纯文本
with open("data/体检数据.csv", "r", encoding="utf-8") as f:
    print(f.read())

# pandas打开
df_csv=pd.read_csv("data/体检数据.csv",index_col=0)
print(df_csv)
# 参数sep表示分割数据的符号，若是数据之间使用=分隔符
# df_csv=pd.read_csv("data/体检数据.csv",index_col=0,sep="=")

# 保存数据到文件
df.to_csv("data/体检数据_sep_修改.csv")
df.to_excel("data/体检数据_sep_修改.xlsx")

print("读保存后的 csv")
print(pd.read_csv("data/体检数据_sep_修改.csv"))

print("读保存后的 xlsx")
print(pd.read_excel("data/体检数据_sep_修改.xlsx"))

# 读取剪切板的数据
df=pd.read_clipboard()
