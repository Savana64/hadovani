greater = 0
st = int(input())
while st !=0:
    nd = int(input())
    if st < nd:
        greater +=1
    st = nd
print(greater)