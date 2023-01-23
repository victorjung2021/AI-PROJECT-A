#첫문장과 두번째문장 동일
with open("text2.txt", "a") as file:
    file.write("안녕하세요.")

file = open("text2.txt", "w")
file.write("안녕하세요.")
file.close()

#첫문장과 두번째문장 동일
with open("text2.txt", "r") as file:
    print(file.read())

file=open("text2.txt", "r")
print(file.read())
file.close()

"""
어떤대상(!)
-텍스트파일
-바이너리파일

어떻게 다룰것인가(!)
-쓰기
 -새로(write): w
 -있는파일 뒤에(append): a
-읽기(read): r
"""