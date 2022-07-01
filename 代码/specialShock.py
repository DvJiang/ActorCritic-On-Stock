# 特殊数据集验证
import pandas as pd
import numpy as np

def make():
    # 参数调整
    stock_code = '0'

    # 获取数据

    data = []
    for i in range(100):
        data.append([i,i+1,i,i+1])
    data = np.array(data)
    name = ['开盘','收盘','最低','最高']
    files = pd.DataFrame(data,columns = name)
    files.to_csv('D:\\'+ stock_code + '.csv')

    print("-------- make Data Done -------")

if __name__ == "__main__":
    make()