import tensorflow as tf
import matplotlib.pyplot as plt


키   = [155,157,160,163,165,170,175,177,179,182,184,186,187,188,190,194,197,199]
신발 = [235,240,245,248,255,256,263,265,267,270,274,276,279,284,286,288,293,297]
a = tf.Variable(0.1)
b = tf.Variable(0.1)
def 손실함수():
    예측값 = 키 * a + b
    return tf.square(신발 - 예측값)
   
opt = tf.keras.optimizers.Adam(learning_rate = 0.2)
 
for i in range(2000):
    opt.minimize(손실함수,var_list=[a,b])
    print(a.numpy(), b.numpy())

#X값의 예상
X=173
print(a * X + b)

fig_size = plt.rcParams['figure.figsize'] = [220,190]
plt.title('Single perceptron learning (x1)')
plt.xlabel('키')
plt.xlabel('신발')
plt.scatter(키,신발, color='black')
plt.scatter(X,a * X + b, color='red')
plt.grid()
plt.show()
