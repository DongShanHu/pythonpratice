import tensorflow as tf

#一定要定義成變量 .Variable() 他才會是個變量
#並且可以給值跟名稱
state=tf.Variable(0,name='counter')
##print(state.name)


one=tf.constant(1)

#新的變量+上一個常量
new_value=tf.add(state,one)

#新的值加載上去
update=tf.assign(state,new_value)

#初始化所有變量(最重要的一部)
init =tf.initialize_all_variables()

#然後用session來激活

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
