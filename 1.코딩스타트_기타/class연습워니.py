class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def say_hello(self,to_name):
     print("안녕!" + to_name + " 나는 " + self.name)
  def introduce(self):
     print("내이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살 입니다")

victor = Person("빅톨",20)
michael = Person("마이클",10)
jenny = Person("제니",13)

victor.say_hello("영희")
michael.say_hello("철수")
jenny.say_hello("미수")

victor.introduce()
