import numpy as np
import tensorflow as tf
import cv2
import os

x0 = tf.compat.v1.placeholder(tf.float32, shape=[1, 256, 256, 1])


def init():
    w0 = tf.Variable(tf.convert_to_tensor(np.load("weight/w0.npy")))
    w1 = tf.Variable(tf.convert_to_tensor(np.load("weight/w1.npy")))
    w2 = tf.Variable(tf.convert_to_tensor(np.load("weight/w2.npy")))
    w3 = tf.Variable(tf.convert_to_tensor(np.load("weight/w3.npy")))
    w4 = tf.Variable(tf.convert_to_tensor(np.load("weight/w4.npy")))
    w5 = tf.Variable(tf.convert_to_tensor(np.load("weight/w5.npy")))
    b0 = tf.Variable(tf.convert_to_tensor(np.load("weight/b0.npy")))
    b1 = tf.Variable(tf.convert_to_tensor(np.load("weight/b1.npy")))
    b2 = tf.Variable(tf.convert_to_tensor(np.load("weight/b2.npy")))
    b3 = tf.Variable(tf.convert_to_tensor(np.load("weight/b3.npy")))
    b4 = tf.Variable(tf.convert_to_tensor(np.load("weight/b4.npy")))
    b5 = tf.Variable(tf.convert_to_tensor(np.load("weight/b5.npy")))
    g = tf.Variable(tf.convert_to_tensor(np.array([1, 2, 4, 8, 16])))
    x1 = tf.nn.relu(tf.nn.conv2d(x0, w0, strides=[1, 2, 2, 1], padding='SAME') + b0)
    x2 = tf.nn.max_pool2d(x1, ksize=[1, 4, 4, 1], strides=[1, 4, 4, 1], padding='SAME')
    x3 = tf.nn.relu(tf.nn.conv2d(x2, w1, strides=[1, 2, 2, 1], padding='SAME') + b1)
    x4 = tf.nn.max_pool2d(x3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    x5 = tf.nn.relu(tf.nn.conv2d(x4, w2, strides=[1, 1, 1, 1], padding='SAME') + b2)
    x6 = tf.nn.max_pool2d(x5, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding='SAME')
    x7 = tf.nn.relu(tf.matmul(tf.reshape(x6, [-1, 8 * 8 * 32]), w3) + b3)
    x8 = tf.nn.relu(tf.matmul(x7, w4) + b4)
    x9 = tf.reduce_sum(tf.cast(tf.greater(tf.matmul(x8, w5) + b5, 0), tf.int32) * g)
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    sess.run(tf.global_variables_initializer())
    return x9, sess


def run(x, answer, s):
    return answer.eval(session=s, feed_dict={x0: np.reshape(x, (1, 256, 256, 1))})


'''
answer, session = init()
a = np.load("G:/DataSet/TestingSet.npy")
for i in range(32):
	print(run(a[i], answer, session))
'''
