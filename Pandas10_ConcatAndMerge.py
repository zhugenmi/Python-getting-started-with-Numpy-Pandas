import pandas as pd

df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}, index=[0, 1, 2, 3],)

df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"],
}, index=[4, 5, 6, 7],)

df3 = pd.DataFrame({
    "A": ["A8", "A9", "A10", "A11"],
    "B": ["B8", "B9", "B10", "B11"],
    "C": ["C8", "C9", "C10", "C11"],
    "D": ["D8", "D9", "D10", "D11"],
}, index=[8, 9, 10, 11],)

# 拼接Concat
pd.concat([df1,df2,df3])
#  加上主key
all_class=pd.concat(
    [df1,df2,df3],
    keys=["x","y","z"]
)
print(all_class)

# 按照key来索引
all_class.loc["y"]

df4 = pd.DataFrame({
    "B": ["B2", "B3", "B6", "B7"],
    "D": ["D2", "D3", "D6", "D7"],
    "F": ["F2", "F3", "F6", "F7"],
}, index=[2, 3, 6, 7],)

# 指定左右拼接 这种模式叫做 join="outer" 的方式（默认方式）， 中文叫它外拼接
print(pd.concat([df1,df4],axis=1))
# 内拼接
print(pd.concat([df1,df4],axis=1,join="inner"))
# ignore_index覆盖老数据索引，刷新索引
pd.concat(
    [df1,df4],
    ignore_index=True,
    sort=False
)

# 添加列数据：把一条新的 col x 数据拼接到了 df1 的最右边
new_col=pd.Series(
    ["x0","x1","x2","x3"],name="x"
)
print(pd.concat([df1,new_col],axis=1))

# 添加行数据
new_row = pd.Series(
    ["X0", "X1", "X2", "X3"],
    index=["A", "B", "C", "D"])
pd.concat(
    [df1, new_row.to_frame().T],
    ignore_index=True)
# 也可以直接append
df1.append(new_row, ignore_index=True)

# 注意：merge 是用来针对两张 df 做【左右】拼接的
left = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})


right = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})
pd.merge(left, right, on="key")

left = pd.DataFrame({
    "key1": ["K0", "K0", "K1", "K2"],
    "key2": ["K0", "K1", "K0", "K1"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})
right = pd.DataFrame({
    "key1": ["K0", "K1", "K1", "K2"],
    "key2": ["K0", "K0", "K0", "K0"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})

pd.merge(left, right, on=["key1", "key2"])
# join的方法：
# outer: 集合两个 df 所有 的 key
# inner: 集合两个 df 同时拥有 的 key
# left: 仅考虑左边 df 所有 的 key
# right: 仅考虑右边 df 所有 的 key
# cross: 对于两个 df key 的笛卡尔积
pd.merge(left, right, how="left", on=["key1", "key2"])

# 接入join，更像merge和concat的结合体
left = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"]
}, index=["K0", "K1", "K2"])


right = pd.DataFrame({
    "C": ["C0", "C2", "C3"],
    "D": ["D0", "D2", "D3"]
}, index=["K0", "K2", "K3"])

left.join(right)