a=[[12,20],[30,40],[50,60],[70,80]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
       


print(a)

 

a=[]
for i in range(3):
    line=[]
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)


a=[['*' for j in range(2)] for i in range(3)]
print(a)

a=[[0] * 2 for i in range(3)]
print(a)

a=[[9] * i for i in [5,4,3,2,1]]
print(a)
