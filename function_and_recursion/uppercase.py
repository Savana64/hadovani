def capitalize(lower_case_word):
    txt = lower_case_word
    x = txt.title()
    return x
print(capitalize(input("input word:\n")))  

def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))