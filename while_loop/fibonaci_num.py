z = int(input())
res = 1
i = 0
j = 0
fib =[0]
while i < z:
    res += j
    i +=2
    fib.append(res)
    j += res
    
    fib.append(j)
if z == 1:
    print(1)
else:
    print(fib[z])