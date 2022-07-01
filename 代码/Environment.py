import pandas as pd
import numpy as np

# 环境搭建
class Env:
    def __init__(self,stock_code, tc):
        self.code = stock_code
        self.data = pd.read_csv('D:\\'+ stock_code + '.csv',encoding="gb2312")
        #self.data = pd.read_csv('D:\\'+ stock_code + '.csv',encoding="utf-8")
        # print(self.data)
        self.lines = 0
        self.tc = tc
        self.maxPrice = 0
        self.money = 0
        self.stocks = []
        self.stock = 0
    
    # 重新开始
    def init_module(self):
        if (self.lines != 0):
            for i in range(self.lines - 1):
                obv = self.observation(i)
                obv = obv[np.newaxis, :]
        obv = self.observation(self.lines)
        rew = 0
        done = 0
        return obv, rew ,done

    # 计算读取各种经济数据
    def observation(self,lines):
        o = self.data['开盘'].values[lines]
        c = self.data['收盘'].values[lines]
        l = self.data['最低'].values[lines]
        h = self.data['最高'].values[lines]
        self.maxPrice = max(c,self.maxPrice)
        return np.array((o, c, l, h))

    # 为限定模型，设置每次只能买或卖，且一次只能买卖一股,0买入,1卖出,2不动
    # 决定买入时，将会以当天的收盘价买入，reward以第二天开盘价计算
    def step(self, action):
        if (action == 0):
            self.stock += 1
            self.money -= self.data['收盘'].values[self.lines]*(1+self.tc)
        elif (action == 1):
            self.stock -= 1
            self.money += self.data['收盘'].values[self.lines]*(1-self.tc)
        self.lines += 1
        self.stocks.append(self.stock)
        rew = self.stock * self.data['开盘'].values[self.lines] + self.money
        #rew = rew - self.maxPrice * self.lines
        obv = self.observation(self.lines)
        if (self.lines >= len(self.data['开盘'].values) - 1): done = 1
        else: done = 0
        return obv, rew ,done
    
    def readLines(self):
        return self.lines

    def readStocks(self):
        return self.stocks

    def readData(self):
        return self.data['开盘'].values

