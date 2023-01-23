import random 
def getRandomNumber():
    number=random.randint(1,45)
    return number
count=0
lotto_number=[]
while True:
    if count > 6:
       break
    random_number = getRandomNumber()
    if random_number not in lotto_number:
       lotto_number.append(random_number)
       count=count+1

print(lotto_number) 
  