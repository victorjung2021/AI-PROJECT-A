#
#  클래스 이해하기 3 진행
#
class 학생:
    def __init__(self, name, korean, math, english):
        self.name= name
        self.korean=korean
        self.math=math
        self.english=english
    def 총점(self):
        return self.korean + self.math + self.english
    def 평균(self):
        return self.총점() / 3
    def 출력(self):
        print(self.name, self.총점(), self.평균(), sep="\t")

students=[
    학생("정형준", 87, 44, 54),
    학생("김찬수", 65, 65, 87),
    학생("김선기", 97, 98, 85),
    학생("정준기", 65, 87, 76),
    학생("정형기", 65, 76, 76),
    학생("정현성", 99, 98, 97)
]  
print("이름","총점","평균",sep="\t")
for student in students:
    student.출력()  




#
#  클래스 이해하기 2 진행
#
#학생 리스트를 선언
# def 학생_생성(name,korean,math,english):
#     return {
#         "name": name,
#         "korean": korean,
#         "math": math,
#         "english": english
#     }
# def 총점(student):
#     return student["korean"] + student["math"] + student["english"]
# def 평균(student):
#     return 총점(student) / 3
# def 출력(student):
#     print(student["name"],총점(student),평균(student),sep="\t")

# students=[
#     학생_생성("정형준", 87, 44, 54),
#     학생_생성("김찬수", 65, 65, 87),
#     학생_생성("김선기", 97, 98, 85),
#     학생_생성("정준기", 65, 87, 76),
#     학생_생성("정형기", 65, 76, 76),
#     학생_생성("정현성", 99, 98, 97)
# ]  
# #학생을 한 명씩 반복합니다.
# print("이름","총점","평균",sep="\t")
# for student in students:
#     #함수활용
#     출력(student)  

#
#  클래스 이해하기 1 진행
#

#학생 리스트를 선언
# students=[
#     {"name":"정형준","korean":87,"영어":44,"과학":65},
#     {"name":"김찬수","korean":65,"영어":65,"과학":87},
#     {"name":"김선기","korean":97,"영어":98,"과학":85},
#     {"name":"정준기","korean":65,"영어":87,"과학":76},
#     {"name":"정형기","korean":65,"영어":76,"과학":76},
#     {"name":"정현성","korean":99,"영어":98,"과학":97}
# ]
# def 총점(student):
#     return student["korean"] + student["영어"] + student["과학"]
# def 평균(student):
#     return 총점(student) / 3
# def 출력(student):
#     print(student["name"],총점(student),평균(student),sep="\t")
  
# #학생을 한 명씩 반복합니다.
# print("이름","총점","평균",sep="\t")
# for student in students:
#     #함수활용
#     출력(student)  
  
# 1번 수행을 함수이용 2번으로 변경
#   for student in students:
#     #점수의 총점과 평균을 구한다
#     score_sum = student["korean"] + student["영어"] + student["과학"]
#     score_average = score_sum / 3
#     #출력 
#     print(student["name"],score_sum,score_average,sep="\t")  