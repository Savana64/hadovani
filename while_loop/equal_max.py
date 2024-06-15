num = int(input())
equal = 1
advice = []
while num !=0:
    advice.append(num)
    num = int(input())
advice.sort()
while len(advice) >= 2:
    if advice[-1] == advice[-2]:
        advice.pop()
        equal += 1
print(equal)