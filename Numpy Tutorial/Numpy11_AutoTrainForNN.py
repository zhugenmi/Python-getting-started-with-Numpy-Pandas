import numpy as np
import matplotlib.pyplot as plt
def draw_scatter(x, y):
    plt.scatter(x.ravel(), y.ravel())
    plt.show()

def draw_line(x, y):
    idx = np.argsort(x.ravel())
    plt.plot(x.ravel()[idx], y.ravel()[idx])
    plt.show()

def layer(in_dim, out_dim):
    weights = np.random.normal(loc=0, scale=0.1, size=[in_dim, out_dim])
    bias = np.full([1, out_dim], 0.1)
    return {"w": weights, "b": bias}

def backprop(dz, layer, layer_in):
    gw = layer_in.T.dot(dz)
    gb = np.sum(dz, axis=0, keepdims=True)
    new_dz = dz.dot(layer["w"].T)
    layer["w"] += learning_rate * gw
    layer["b"] += learning_rate * gb
    return new_dz

def predict(x):
    o1 = x.dot(l1["w"]) + l1["b"]
    a1 = relu(o1)   # 这里我添加了一个激活函数
    o2 = a1.dot(l2["w"]) + l2["b"]
    return [o1, a1, o2]

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):     # 导数
    return np.where(x > 0, np.ones_like(x), np.zeros_like(x))

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):     # 导数
    return 1 - np.square(np.tanh(x))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):  # 导数
    o = sigmoid(x)
    return o * (1 - o)

# 线性数据
x = np.linspace(-1, 1, 10)[:, None]     # shape [10, 1]
y = np.random.normal(loc=0, scale=0.2, size=[10, 1]) + x   # shape [10, 1]
# 非线性数据
# x = np.linspace(-1, 1, 30)[:, None]     # shape [30, 1]
# y = np.random.normal(loc=0, scale=0.2, size=[30, 1]) + x**2   # shape [30, 1]


# 构建模型
l1 = layer(1, 3)
l2 = layer(3, 1)

# 没有训练时
draw_line(x, predict(x)[-1])
draw_scatter(x, y)

# 计算
o = x.dot(l1["w"]) + l1["b"]
print("第一层出来后的 shape:", o.shape)

o = o.dot(l2["w"]) + l2["b"]
print("第二层出来后的 shape:", o.shape)

print("output:", o)
draw_scatter(x, o)

# 训练 300 次
learning_rate = 0.01
for i in range(300):
    # 前向预测
    o1, a1, o2 = predict(x)

    # 误差计算
    if i % 10 == 0:
        average_cost = np.mean(np.square(o2 - y))
        print(average_cost)

    # 反向传播，梯度更新
    dz2 = -2 * (o2 - y)  # 输出误差 (o2 - y)**2 的导数
    dz1 = backprop(dz2, l2, a1)
    dz1 *= relu_derivative(o1)  # 这里要添加对应激活函数的反向传播
    _ = backprop(dz1, l1, x)

draw_line(x, predict(x)[-1])
draw_scatter(x, y)