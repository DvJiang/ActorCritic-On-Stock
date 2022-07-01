from turtle import color
from ACSDK import Actor,Critic 
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import Environment
import getShock

GAMMA = 0.1  # 衰变值
LR_A = 0.0001  # Actor学习率
LR_C = 0.5  # Critic学习率

N_F = 4  # 状态空间
N_A = 3  # 动作空间

def main():
    # 数据设定
    stock_code = '000037'
    trade_cost = 15/10000

    #getShock.get(stock_code)

    sess = tf.compat.v1.Session()
    actor = Actor(sess, n_features=N_F, n_actions=N_A, lr=LR_A)  # 初始化Actor
    critic = Critic(sess, n_features=N_F, lr=LR_C)  # 初始化Critic
    sess.run(tf.compat.v1.global_variables_initializer())  # 初始化参数

    env = Environment.Env(stock_code, trade_cost)
    obv, reward, done = env.init_module()
    rewards = []
    td_errors = []
    vs = []
    print(obv)
    while(True):
        action = actor.choose_action(obv)
        obv_, reward, done = env.step(action)
        rewards.append(reward)
        td_error,v_1 = critic.learn(obv, reward, obv_)
        td_errors.append(td_error[0])
        vs.append(v_1[0])
        actor.learn(obv, action, td_error)
        obv = obv_
        #print(reward)
        if (done):break
    
    x = np.linspace(0,env.readLines()-1,env.readLines())
    plt.plot(x,np.array(rewards),color = 'blue')
    plt.plot(x,np.array(vs),color = 'black')
    plt.plot(x,100 * np.array(env.readData())[1:],color = 'red')
    plt.plot(x,100 * np.array(env.readStocks())[0:],color = 'yellow')
    plt.show()



if __name__ == "__main__":
    main()







