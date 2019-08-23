import tensorflow as tf

a = tf.Variable(10) #10: gia tri se duoc khoi tao ban dau
b = tf.Variable(29) #29: gia tri se duoc khoi tao ban dau
#a, b chua co gia tri den khi no duoc khoi tao trong phien(session)

c = tf.add(a,b)
#Ham khoi tao gia tri ban dau cho cac bien x,y
#chu y: Khac voi lap trinh thong thuong, day moi dung lai o viec dinh nghia ham
#Ham initialize_all_variables() chua thuc su chay, x va y node chua he co gia tri
init = tf.initialize_all_variables()
init = tf.initialize_all_variables()

#Chay Graph
with tf.Session() as sess:
    # tf.initialize_all_variables luc nay chay thuc su -> cac node x, y moi bat dau co gia tri
    sess.run(init)
    sess.run(c) #Chay Graph
    print(c.eval())

writer = tf.summary.FileWriter

