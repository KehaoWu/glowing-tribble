# @Author: wukehao
# @Date:   2017-09-18T21:22:35+08:00
# @Last modified by:   wukehao
# @Last modified time: 2017-09-18T21:24:28+08:00



import numpy as np
import tensorflow as tf

sess = tf.Session()
m = sess.run(tf.truncated_normal((5,10, 4), stddev = 0.1) )
print (type(m))
print (m)

col_max = sess.run(tf.argmax(m, 0) )  #当axis=0时返回每一列的最大值的位置索引
print (col_max)

row_max = sess.run(tf.argmax(m, 1) )  #当axis=1时返回每一行中的最大值的位置索引
print (row_max)
