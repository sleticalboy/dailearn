import numpy as np

if __name__ == '__main__':
    print(np.ones((2,), dtype=np.int8))
    print(np.zeros((2,), dtype=np.int8))

    # 产生随机点
    print(np.linspace(0, 10, num=10, dtype=np.int8))
    # 产生坐标数组
    print(np.meshgrid([1, 2, 3]))
    print(np.random.rand(3, 2))
    # 产生随机整数
    print(np.random.randint(6, size=10))
    # 四舍五入
    print(np.round(3.1415, 3))
    # 向下向上取整
    print(np.floor(3.1415))
    print(np.ceil(3.1415))
    print(np.cumsum([1, 2, 3, 4]))  # 累加
    print(np.cumprod([1, 2, 3, 4]))  # 累乘
    pass
