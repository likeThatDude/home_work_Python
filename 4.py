words = 'a a a b c a a d c d d'
words = words.split(' ')
digit = {}


res = ''
for i in words:
    if i in digit:
        res += f'{i}_{digit[i]} '
        digit[i] += 1
        print(digit)
    else:
        res += f'{i} '
        digit[i] = 1
        print(digit)
print(res)