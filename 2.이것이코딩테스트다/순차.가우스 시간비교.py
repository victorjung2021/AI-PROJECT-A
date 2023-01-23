import time
start_time =time.time()

sum = 0    
n = 100

for i in range(1, n+1):
   sum = sum + i
print(sum)

print("1부터 {}까지 합은 {} 입니다".format(n,sum))    

end_time = time.time()
print("1 time :" , end_time - start_time)

start_time =time.time()
sum= (1+n) * (n/2)
print(sum)
end_time = time.time()
print("2 time :" , end_time - start_time)
    
    
