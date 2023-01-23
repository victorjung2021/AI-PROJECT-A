import random
numList = (588, 18, 71, 113, 5, 12, 3, 320, 4, 7)

for k in range(10):
    cntSum=0
    for i in range(10000):
        rndNum=numList[random.randint(0,9)]
        for n in numList:
            cntSum = cntSum + 1
            if n ==rndNum:
                break
    print(cntSum/10000)