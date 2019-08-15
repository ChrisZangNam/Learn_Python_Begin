import tensorflow as tf

a = tf.constant([
    [1,2,3],
    [4,5,6]
])

b = tf.constant([
    [3,4,5],
    [6,7,8]
])

c = tf.add(a,b)

with tf.Session() as sess:
    sess.run(c)
    print(c.eval())
