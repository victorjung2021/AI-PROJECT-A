class Student:
    def __init__(self,이름,나이):
        print("객체가 생성")
        self.이름 = 이름
        self.나이 = 나이
    def __del__(self):
        print("객체소멸")
    def 출력(self):
        print(self.이름,self.나이)

student=Student("정형준",45)
student.출력()
     