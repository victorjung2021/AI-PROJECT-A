#아래 2개 프린트문 동일결과
a=list(range(100))
print(list(map(lambda number: number * number, a)))
print([i * i for i in a if i % 2 ==0])


#아래 filter힘수를 람다로 대체
a= list(range(100))
b= filter(lambda number: number % 2 == 0,a)
print(list(b))
#아래처럼 프린트 혹은 리스트로 만들어서 프린트 동일
# for i in b:
#     print(i)

# def 짝수만(number):
#     return number % 2 ==0
# a= list(range(100))
# b= filter(짝수만,a)
# print(list(b))
#아래처럼 프린트 혹은 리스트로 만들어서 프린트 동일
# for i in b:
#     print(i)



# #콜백함수 함수, lambda함수
# def call_10_times(func):
#     for i in range(10):
#         func(i)

# call_10_times(lambda number: print("안녕하세요", number))

# #콜백함수 함수에서 함수를 콜
# def call_10_times(func):
#     for i in range(10):
# #콜백함수
#         func(i)
# def print_hello(number):
#     print("안녕하세요", number)

# call_10_times(print_hello)

