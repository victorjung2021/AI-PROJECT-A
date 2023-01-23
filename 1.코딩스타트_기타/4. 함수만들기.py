def sum(a, b):
    return a + b
print(sum(3, 5)) 


def add_suffix(name):
    return name + '님' 
print(add_suffix('정형준'))  

def hello():
    name=input('이름은 무엇인가요?')
    print(name,'님, 반갑습니다.')
hello()

def hello(name,greeting):
    print(name,'님', greeting)
hello('정형준','반갑네요') 

