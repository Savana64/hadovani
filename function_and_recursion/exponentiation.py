def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a,n-1)
a=float(input("mocněnec\n")) 
n=int(input("mocnitel\n"))

print(power(a,n))
    
