import tensorflow as tf
import matplotlib.pyplot as plt


xxx  = [1,2,3]
yyy = [1,2,3]
a = tf.Variable(0.1)
b = tf.Variable(0.1)
def 손실함수():
    예측값 = xxx * a + b
    return tf.square(yyy - 예측값)
   
opt = tf.keras.optimizers.Adam(learning_rate = 0.2)
 
for i in range(200):
    opt.minimize(손실함수,var_list=[a,b])
    print(a.numpy(), b.numpy(),손실함수)

#X값의 예상
X=4
print(a * X + b)

fig_size = plt.rcParams['figure.figsize'] = [220,190]
plt.title('Single perceptron learning (x1)')
plt.xlabel('xxx')
plt.xlabel('yyy')
plt.scatter(xxx,yyy, color='black')
plt.scatter(X,a * X + b, color='red')
plt.grid()
plt.show()
