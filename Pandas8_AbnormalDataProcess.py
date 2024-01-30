import pandas as pd
import numpy as np

df = pd.DataFrame([[1, None],[np.nan, 4]])
# 找到NaN数据
df.isna()
df.notna() # equal to  ~df.isna()

df = pd.DataFrame({
    "a": [1, None, 1],
    "b": [np.nan, 4, 4]
})
print("skipped NaN:\n", df.mean(axis=0))
print("\n\nnot skipped:\n", df.mean(axis=0, skipna=False))

# 丢弃NaN， axis=0 的时候，如果某一 row 有 NaN，就会丢弃这一 row。同理 axis=1 的时候， column 有 NaN 丢弃 column
df.dropna(axis=0)

# 填充NaN，可以用均值填充，或者默认值填充
a_mean=df["a"].mean()
new_col=df["a"].fillna(a_mean)
df["a"]=new_col
print(df)

# 当数据明显有一定的规律时，比如发现b是a的4倍，就可以根据规律填充
df = pd.DataFrame({
    "a": [1, None, 3, None],
    "b": [4, 8, 12, 12]
})
a_nan = df["a"].isna()
a_new_value = df["b"][a_nan] / 4
new_col = df["a"].fillna(a_new_value)
df["a"] = new_col
# 或者直接给a列赋值
df.loc[a_nan, "a"] =  df["b"][a_nan] / 4

# 处理不符合范围的值
df = pd.DataFrame({
    "a": [1, 1, 2, 1, 2, 40, 1, 2, 1],
})

df["a"] = df["a"].clip(lower=0, upper=3)
df.plot()
