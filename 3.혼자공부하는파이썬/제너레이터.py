def 함수():
    print("출력a")
    yield 100
    print("출력b")
    yield 200
    print("출력c")
    yield 300
    

제너레이터 = 함수()

for i in 제너레이터:
    print(i)

for i in 제너레이터:
    print(i)

numbers=[1,2,3,4,5]
이터레이터 =reversed(numbers)
for i in 이터레이터:
    print(i)
for i in 이터레이터:
    print(i)





#print("#홀수만 추출하기")
#print(list(filter(lambda x: x % 2 ==1,numbers)))
#rint()

#print("#3이상,7미만 추출하기")
#print(list(filter(lambda x: 3<= x <7,numbers)))
#print()

#print("#제곱이 50미만 추출하기")
#print(list(filter(lambda x: x ** 2 < 50 ,numbers)))
#print()