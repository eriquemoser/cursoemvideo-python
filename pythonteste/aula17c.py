a = [2,3,4,7]
#b = a
b = a[:]

b[2] = 8

print(f'A lista a é {a}')
print(f'A lista b é {b}')