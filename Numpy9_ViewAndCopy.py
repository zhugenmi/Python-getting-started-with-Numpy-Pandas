# view--给源数据加一个窗口，类似于直接引用，而copy会新建数据
import numpy as np
import timeit
from functools import partial

def get_run_time(func, *args):
    repeat = 3
    number = 200
    return min(timeit.Timer(partial(func, *args)).repeat(repeat=repeat, number=number)) / number


a = np.arange(1, 7).reshape((3,2))
a_view = a[:2]
a_copy = a[:2].copy()

a_copy[1,1] = 0
print("在 copy 上修改数据，不会影响源数据：\n", a)

a_view[1,1] = 0
print("在 view 上修改数据，会影响'窗里'的源数据：\n", a)

a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)

# 把矩阵展平
def f1():
    a.flatten() # 返回一个copy

def f2():
    b.ravel()

print('%.6f - flatten' % get_run_time(f1))
print('%.6f - ravel' % get_run_time(f2))

# view方式选择数据避免copy
a = np.zeros([100, 100])
a_view1 = a[1:2, 3:6]    # 切片 slice
a_view2 = a[:100]        # 同上
a_view3 = a[::2]         # 跳步
a_view4 = a.ravel()      # 上面提到了

# 下面的操作是copy
a = np.zeros([2, 2])
a_copy2 = a[[True, True], [False, True]]  # 用 mask
a = np.zeros([100, 100])
a_copy1 = a[[1,4,6], [2,4,6]]   # 用 index 选
a_copy3 = a[[1,2], :]        # 虽然 1,2 的确连在一起了, 但是他们确实是 copy
a_copy4 = a[a[1,:] != 0, :]  # fancy indexing
a_copy5 = a[np.isnan(a[:,0]), :]  # fancy indexing

# 使用 np.take(), 替代用 index 选数据的方法。
# 如果用 index 来选数据, 像 a_copy1 = a[[1,4,6], [2,4,6]], 用 take 在大部分情况中会比这样的 a_copy1 要快。
a = np.random.rand(1000000, 10)
indices = np.random.randint(0, len(a), size=10000)

def f1():
    # fancy indexing
    _ = a[indices]

def f2():
    # take
    _ = np.take(a, indices, axis=0)

print('%.6f - [indices]' % get_run_time(f1))
print('%.6f - take' % get_run_time(f2))

# 使用 np.compress(), 替代用 mask 选数据的方法。
a = np.random.rand(10000, 10)
mask = a[:, 0] < 0.5


def f1():
    _ = a[mask]


def f2():
    _ = np.compress(mask, a, axis=0)


print('%.6f - [mask]' % get_run_time(f1))
print('%.6f - compress' % get_run_time(f2))

# 使用参数out，可以利用这种特性来减少 copy 的产生
a = np.zeros([1000, 1000])
b = np.zeros_like(a)
c = np.zeros_like(a)

def f1():
    a[:] = np.add(a, 1)  # 把计算结果赋值回原数据

def f2():
    np.add(b, 1, out=b)  # 把计算结果赋值回原数据

def f3():
    _c = np.add(c, 1)   # 把计算结果赋值到新数据


print('%.6f - without out' % get_run_time(f1))
print('%.6f - out' % get_run_time(f2))
print('%.6f - new data' % get_run_time(f3))