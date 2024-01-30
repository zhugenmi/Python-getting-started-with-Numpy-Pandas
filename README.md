# Python-getting-started-with-Numpy-Pandas

快速入门python编程语言，包含python语言基础，Numpy教程，Pandas教程代码。

# Python 语言快速入门
[Start Coding](StartCoding.py)

# Numpy 教程
`Numpy`可以很快速的处理多维数据，其运行速度很快。

## 维度处理

`Numpy`中，主要涉及维度的方法有

- 创建数据
  - `np.array()`
  - `array.ndim`
- 添加数据
  - `np.concatenate()`
  - `np.expand_dims()`
- 合并数据
  - `np.concatenate()`
  - `np.vstack()`
  - `np.hstack()`
- 观察形态
  - `array.size`
  - `array.shape`

参考代码：[DimensionProcess.py](Numpy1_DimensionProcess.py)

## 数据选择

- 单个选取
  - `array[1]`
  - `array[1,2,3]`
  - `array[1][1]`
- 切片划分
  - `array[:3]`
  - `array[2:4, 1:3]`
- 条件筛选
  - `array[array<0]`
  - `np.where(array, array < 0)`

参考代码：[DataSelect.py](Numpy2_DataSelect.py)

## 基础运算

- 加减乘除
  - `+-*/`
  - `np.dot()`
- 数据统计分析
  - `np.max() np.min() np.sum() np.prod() np.count()`
  - `np.std() np.mean() np.median()`
- 特殊运算符号
  - `np.argmax() np.argmin()`
  - `np.ceil() np.floor() np.clip()`

参考代码：[BasicOperations.py](Numpy3_BasicOperations.py)

## 数据形态转变

- 改变形态
  - `array[np.newaxis, :]`
  - `array.reshape()`
  - `array.ravel(), array.flatten()`
  - `array.transpose()`
- 合并
  - `np.column_stack(), np.row_stack()`
  - `np.vstack(), np.hstack(), np.stack()`
  - `np.concatenate()`
- 拆解
  - `np.vsplit(), np.hsplit(), np.split()`

参考代码：[ChangeDataFormat.py](Numpy4_ChangeDataFormat.py)

## 读取保存数据

- 加载常用数据格式
  - `np.loadtxt(), np.fromstring()`
- 保存数据
  - `np.savetxt()`
  - `np.save(), np.savez(), np.savez_compressed()`

## 标准数据生成

- 创建统一数据
  - `np.zeros(), np.ones(), np.full()`
  - `np.zeros_like(), np.ones_like(), np.full_like()`
- 创建规则数据
  - `np.arange(), np.linspace()`
- 快速创建再添加值
  - `np.empty(), np.empty_like()`

参考代码：[DataGenerating.py](Numpy7_DataGenerating.py)

## 随机数和随机操作

- 多种随机数生成
  - `np.random.rand(), np.random.random()`
  - `np.random.randn(), np.random.randint()`
- 给你施加随机
  - `np.random.choice()`
  - `np.random.shuffle(), np.random.permutation()`
- 随机分布
  - `np.random.normal(), np.random.uniform()`
- 随机种子的重要性
  - `np.random.seed()`

参考代码：[Random.py](Numpy8_Random.py)

## 其他
Numpy中的`view`与`copy`：[ViewAndCopy.py](Numpy9_ViewAndCopy.py)

使用**Numpy**对疫情数据进行分析：[Numpy_EpidemicDataAnalysis.py](Numpy5_EpidemicDataAnalysis.py)

使用**Numpy**对数据进行预处理：[DataClean.py](Numpy6_DataClean.py)

使用**Numpy**进行矩阵运算：[MatrixOperation.py](Numpy10_MatrixOperationForNN.py)

使用**Numpy**完成神经网络：[AutoTrainForNN.py](Numpy11_AutoTrainForNN.py)

**Numpy Reference**：<https://numpy.org/doc/stable/reference/index.html#reference>

# Pandas 教程
Pandas 是 Python 中一个比较常用的第三方库，里面集成了很多和数据相关的功能组件，如处理数据、分析数据、画图等。它承接了 Numpy 的能力，使用的底层也是 Numpy。这就导致了其**运算速度稍微比 Numpy 慢。**

Pandas 首先支持的是序列数据和表格数据，Pandas 中的 Series 的核心其实就是一串类似于 Python List 的序列，Numpy 和 List 可以用来创建 Series， Series 也能回退到 Numpy array 或者 List。而常见的二维数据表可以通过Pandas 的 DataFrame 维护。代码示例：[SeriesAndDataFrame.py](Pandas2_SeriesAndDataFrame.py)

## 基本操作

### 从文件读取数据

- Excel文件
  - `pd.read_excel()`
  - `df.to_excel()`
- csv或txt等纯文本文件
  - `pd.read_csv()`
  - `df.to_csv()`
- 其他有趣的
  - `pd.read_clipboard()`
  - `pd.read_html()`

参考代码：[ReadData.py](Pandas1_ReadData.py)

### 选取数据

- 选Column
- loc
- iloc
- loc和iloc混搭
- 条件过滤筛选
- Series和DataFrame类似

参考代码：[DataSelect.py](Pandas3_DataSelect.py)

### 基础统计方法

- 均值中位数 df.mean()；df.median()
- 累加累乘 df.sum()；df.prod()
- 最大最小 df.max(); df.min()
- 处理空值 df.isnull(); df.notnull(); df.dropna(); df.fillna()
- 获取索引 `df.idxmin(); df.idxmax()`

参考代码：[BasicStaticsMethods.py](Pandas4_BasicStaticsMethods.py)

### 数据可视化技术

- 散点图 scatter
- 折线图 plot
- 条形图 bar
- 分布图 histograms
- 饼图 pie
- 面积图 area

参考代码：[Draw.py](Pandas5_Draw.py)

## 数据处理

在Pandas中有效筛选数据后，有时候需要进行计算，两种运算方法：筛选赋值运算、Apply方法。

参考代码：[OperationalMethods.py](Pandas6_OperationalMethods.py)

### 文字处理

- 格式化字符
  - `str.upper(); str.lower(); str.len()`
  - `str.strip(); str.lstrip(); str.rstrip()`
  - `str.split()`
- 正则方案
  - `str.contains(); str.match(); str.startswith(); str.endswith()`
  - `str.replace()`
  - `str.extract(); str.extractall()`
- 拼接
  - `str.cat()`

参考代码：[StrProcess.py](Pandas7_StrProcess.py)

### 异常数据处理

- 找到NaN数据

  - `pd.isna(), pd.notna()`

- 移除NaN

  - `df.dropna()`

- 填充NaN

  - `df.fillna()`

- 不符合范围的值

  - `df.clip()`

参考代码：[AbnormalDataProcess.py](Pandas8_AbnormalDataProcess.py)

### 时间数据

- 读时间序列数据
  - `pd.to_datetime()`
- 自建时间序列
  - `pd.date_range()`
- 选取时间
- 时间运算
  - `pd.Timedelta()`
  - `dt.dayofyear; dt.dayofweek; dt.weekofyear; dt.weekday`
  - `dt.strftime(); dt.day_name(); dt.month_name()`
- 时区
  - `tz_localize(); tz_convert()`
  - `pytz.country_timezones()`

参考代码：[TimeDataProcess.py](Pandas9_TimeDataProcess.py)

## 数据管理

### Concat 和 Merge

主要有

- 拼接 Concat
- 融合 Merge
- 接入 Join

参考代码：[ConcatAndMerge.py](Pandas10_ConcatAndMerge.py)

  ### 数据分组Groupby

- 分组
  - `df.groupby(); grouped.groups; grouped.get_group()`
- 调用分好的组
  - grouped.first(); grouped.last()
- 循环处理
- 多从分组
- 聚合计算
  - `grouped.agg()`

参考代码：[Groupby.py](Pandas11_Groupby.py)

### 多索引Multi-Indexing

- 构建Row多索引
  - `from_tuples(); from_product(); from_frame()`
- 构建DataFrame多索引
- 构建Column多索引
- 选择数据

参考代码：[Multi-Indexing.py](Pandas12_Multi-Indexing.py)

## 其他

使用**Pandas**对疫情数据进行分析：[Pandas_EpidemicDataAnalysis.py](Pandas13_EpidemicDataAnalysis.py)

使用**Pandas**对数据进行预处理：[Pandas_DataPreprocess.py](Pandas14_DataPreprocess.py)

**Pandas Reference**：<https://pandas.pydata.org/docs/reference/index.html#api>