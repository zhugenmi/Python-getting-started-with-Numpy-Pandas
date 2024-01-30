import pandas as pd

path="data/iris.csv"
columns= ["sepal length", "sepal width", "petal length", "petal width", "class"]
df = pd.read_csv(path, names=columns)
print(df)

# NaN数据处理
print(df.isna().any()) # 找到有空值的column
print(
    df.loc[pd.isna(df["petal width"])] # 定位有空值的那一行数据
)

df1 = df.dropna(axis=0, how="any") # 丢弃存在空值的一行
print(df1.isna().any())

# 异常值处理
df1.plot() # 通过画图方式有没有peek不符合预期
df1["sepal length"].plot() # 或者一条一条画，发现存在负值

index = df1[df1["sepal length"]<0].index
df2 = df1.drop(index)
df2["sepal length"].plot()
df2["sepal length"].hist(bins=20) # 查看分布

# 划分训练、测试数据集
total_data = len(df2)
n_train = int(total_data * 0.8)

df3 = df2.sample(frac=1) # Pandas 的 .sample() 功能能对整个数据在 row 上乱序
train_data = df3.iloc[:n_train]
test_data = df3.iloc[n_train:]

def get_xy(df): # 做标签的切分
    return df[["sepal length", "sepal width", "petal length", "petal width"]], df[["class"]]

train_x, train_y = get_xy(train_data)
print(train_x.head())
print(train_y.head())

test_x, test_y = get_xy(test_data)
print(test_x.head())
print(test_y.head())

# 进一步将 Pandas 的 DataFrame 转成 Numpy array。
train_x_array, train_y_array = train_x.values, train_y.values
print(train_x_array[:3])