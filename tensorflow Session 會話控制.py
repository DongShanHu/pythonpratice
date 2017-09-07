import tensorflow as tf
matrix = tf.constant([[3,3]])
matrix2=tf.constant([[2],[2]])

product=tf.matmul(matrix,matrix2) ##matrix multiply np.dot(m1,m2)

##sess=tf.Session()
##result=sess.run(product)
##print(result)
##
##sess.close()

##with 寫法 打開了session 以sess 來命名 在with 語句之內 就可以不用寫close

with tf.Session() as sess:
    result2=sess.run(product)
    print(result2)
    
