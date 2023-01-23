#재귀함수이용 폴더 파일구분
import os
#폴더를 읽어들이는 함수
def read_folder(path):
    #폴더의 요소 읽어 들이기
    output=os.listdir(path)
    #폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(path + "/" + item):
           #폴더면 계속 읽어들이기
           read_folder(path + "/" + item)
        else:
           #파일이면 출력
           print("파일:",item)
#현재 폴더의 파일/폴더를 출력하기
read_folder(".")             

# import os
# #현재 폴더의 파일/폴더를 출력
# output = os.listdir(".")
# print("os.listdir():",output)
# print()

# #현재 폴더의 파일/폴더를 구분합니다.
# print("# 폴더와 파일 구분하기")
# for path in output:
#     if os.path.isdir(path):
#         print("폴더",path)
#     else:
#         print("파일:",path)



# # 모듈읽어보는방법
# math = __import__("math")
# import math
# import math as 수학
# from math import pi,sin
# from math import *

# print(pi)
# print(수학.pi)
# print(math.pi)

# from datetime import datetime

# now=datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# now=datetime(2021,11,11,11,11,11)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# a찍고 2초 쉬었다 b찍기 
# import time
# print("a")
# time.sleep(2)
# print("b")


# from urllib import request

# target = request.urlopen("http://hanbit.co.kr")
# content = target.read()

# print(content)