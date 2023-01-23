array1=[i for i in range(10) if i % 2 == 0]
array2=[i for i in range(0,10,2)]
array3=[1 for i in range(10)]
print(array1)
print(array2)
print(array3)

#1-100/2진수/0이 하나 이상인 숫자
output=[i for i in range(1,100+1) if "{:b}".format(i).count("0") ==1]
print("합계: {}".format(sum(output)))