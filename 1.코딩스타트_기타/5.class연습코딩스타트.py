class Monster:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print(f'나는 {self.name}이고 {self.age}살 입니다.')

shark = Monster("상어",12)
wolf = Monster("늑대",23)

shark.say()
wolf.say()