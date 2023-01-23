import tensorflow as tf
텐서 = tf.constant([3,4,5])
텐서2 = tf.constant([6,7,8])
#print(텐서+텐서2)

텐서3=tf.constant( [ [1,2,3],
                     [3,4,4]  ])
텐서4=tf.constant( [ [1,2],
                     [3,4],
                     [3,4]])
#print(tf.add(텐서,텐서2))
#print(텐서 / 텐서2)

print(tf.matmul(텐서3,텐서4))
#tf.add()
#tf.subtract()
#tf.divide()
#tf.multiply()
#tf.matmul()
#텐서4 = tf.zeros(10)
#print(텐서4)
#텐서5 = tf.zeros([2,2])
#print(텐서5)
#텐서6 = tf.zeros([2,2,3])
#print(텐서6)

#print(텐서.shape)
#print(텐서3.shape)

#텐서7 = tf.constant([6,7,8],tf.float32)

#weight저장하고 싶으면 Variable만들기
#w = tf.Variable(1.0)
#print(w)
#print(w.numpy())
#w.assign(2)
#print(w)

#더 쉽게 neural network만들기 가능하니 참고만 해두자