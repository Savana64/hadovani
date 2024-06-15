z = int(input())
res = 1
i = 0
j = 0
fib =[0]
while fib[i] < z:
    res += j
    fib.append(res)
    j += res
    i +=2
    fib.append(j)
if z in fib:
    print(fib.index(z))
else:
    print("-1")