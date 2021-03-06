import tensorflow as tf
import numpy as np
import gym
from gym.spaces import Discrete, Box

def mlp(x, sizes, activation=tf.tanh, outputf_activation=None):
    # Build a feedforward neural
    # Question: x为输入，n维向量；sizes为列表，每层的神经元数目
    for size in sizes[:-1]:
        x=tf.layers.dense(x, units=size, activation= activation)
    return tf.layers.dense(x, units=sizes[:-1], activation= outputf_activation)

def train(env_name='CarPole-v0', hidden_size=[32], lr=1e-2,
          epochs=50, batch_size=5000, render=False):

    # make environment, check spaces, get obs / act dims
    env=gym.make(env_name)
    # assert的意义：
    # isinstance判断一个变量是否属于某一类型：isintance(a, int)
    assert isinstance(env.observation_space, Box), \
        "This example only works for envs with continuous state spaces."
    assert isinstance(env.action_space,Discrete), \
        "This example only works for envs with discret action spaces."

    obs_dim=env.observation_space[0]
    n_acts=env.action_space.n

    # 1. Making the Policy Network
    # make core of policy network
    obs_ph=tf.placeholder(shape=(None,obs_dim),dtype=tf.float32)
    logits=mlp(obs_ph,sizes=hidden_size+[n_acts])

    # make action selection op (outputs int actions, sampled from policy)
    actions=tf.squeeze(tf.multinomial(logits=logits,num_samples=1),axis=1)

    # 2. Making the Loss Function
    # make loss function whose gradient, for the right data, is policy gradient
    weights_ph=tf.placeholder(shape=(None,),dtype=tf.float32)
    act_ph=tf.placeholder(shape=(None,),dtype=tf.int32)
    action_masks=tf.one_hot(act_ph,n_acts)
    log_probs=tf.reduce_sum(action_masks*tf.nn.log_softmax(logits),axis=1)
    loss=-tf.reduce_mean(weights_ph*log_probs)

    #













