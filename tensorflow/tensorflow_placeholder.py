import tensorflow as tf
#可以給予類似兩行兩列的input
##input1 =tf.placeholder(tf.float32,[2,2])
input1 =tf.placeholder(tf.float32)
#placeholder 從外界傳入的值 用不同得值來代替

input2 =tf.placeholder(tf.float32)

#mul -->multify 相乘
output=tf.mul(input1,input2)

#placeholder型式要傳入參數
#dic-->dictionary型別
with tf.Session() as sess: 
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))
