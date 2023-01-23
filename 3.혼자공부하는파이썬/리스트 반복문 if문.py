# import datetime
# now=datetime.datetime.now()
# if now.hour < 12:
#     print("현재시간은{}시 {}분 오전입니다.".format(now.hour,now.minute))
# if now.hour > 12:
#     print("현재시간은{}시 {}분 오후입니다.".format(now.hour,now.minute))

# #"{}년 {}월 {}일 {}요일".format(2021, 9, 22, "금")

# numbers=[10,200,30,40,500,32]
# for number in numbers:
#     if number >=100:
#        print("이 숫자{}는 100보다 큽니다.".format(number))

# numbers=[10,201,30,41,505,31]
# for number in numbers:
#     if number % 2 == 0:
#        print("이 숫자 {}는 짝수입니다.".format(number))
#     else:
#        print("이 숫자 {}는 홀수입니다.".format(number))

# numbers=[1,2,3,4,5,6,7,8,9]
# output=[[],[],[]]
# for number in numbers:
#     output[number % 3].append(number)

# print(output)

# numbers=[11,32,53,44,45,46,67,98,49]
# odd_even=["짝수","홀수"]
# for number in numbers:
#     print("{}는 {}입니다.".format(number,odd_even[number % 2]))


numbers=[1,4,5,6,7,8,4,5,6,7,18,3,4,5,2,3,4,5,6,3,4,5,6,1,2,2]
# counter={}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1

# print(counter)     

print(numbers.index(18))
print(18 in numbers)