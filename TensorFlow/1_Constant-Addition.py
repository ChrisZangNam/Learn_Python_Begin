import tensorflow as tf

#x,y duoc goi la Tensor
x = tf.constant(4)
y = tf.constant(5)

z = tf.add(x,y) #Ham cong
with tf.Session() as sess:
    #x, y o day moi bat dau co gia tri
    result = sess.run(z)
    print(z.eval())
