import tensorflow as tf
xData = [1,2,3,4,5,6,7]
yData = [220,550,750,1100,1280,1550,1800]

a = tf.Variable(0.1)
b = tf.Variable(0.2)
def 손실함수():
    예측값 = xData * a + b
    print(xData * a + b)
    return tf.square(yData - 예측값)
   
opt = tf.keras.optimizers.Adam(learning_rate = 0.3)
 
for i in range(3000):
    opt.minimize(손실함수,var_list=[a,b])
    print(a.numpy(), b.numpy())


print("result=", a.numpy(), b.numpy())

##예측값 확인
pre = 8
yy = a.numpy() * pre + b.numpy()
print("테스트값== ", yy)