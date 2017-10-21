import tensorflow as tf
##import numpy as np
##
###create data
##x_data = np.random.rand(100).astype(np.float32)
##y_data = x_data*0.1 + 0.3
##
####create tensorflow structure
##
###1維結構 初始值-1 - 1
##Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
###初始範圍給0
##Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
##biases = tf.Variable(tf.zeros([1]))
##
##y = Weights*x_data + biases
##
##loss = tf.reduce_mean(tf.square(y-y_data))#建造一個優化器來減少誤差 增強學習 學習效率為0.5
##optimizer = tf.train.GradientDescentOptimizer(0.5)
##train = optimizer.minimize(loss)
##
##init = tf.initialize_all_variables()
##
####初始化
##
##sess = tf.Session()
##sess.run(init)
##
##for step in range(201):
##    sess.run(train)
##    if step % 20 == 0:
##        print(step, sess.run(Weights), sess.run(biases))


#Session 為一個執行語句 用於實行參數
        

matrix = tf.constant([[3,3]])
matrix2=tf.constant([[2],[2]])

product=tf.matmul(matrix,matrix2) ##matrix multiply np.dot(m1,m2)

sess=tf.Session()
result=sess.run(product)
print(result)

sess.close()

##with 寫法 打開了session 以sess 來命名 在with 語句之內 就可以不用寫close
##
##with tf.Session() as sess:
##    result2=sess.run(product)
##    print(result2)
    
