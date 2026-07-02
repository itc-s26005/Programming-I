#a, r1 = divmod(23, 2)
#a, r1 = divmod(a, 2)
#a, r1 = divmod(a, 2)
#a, r1 = divmod(a, 2)
#a, r1 = divmod(a, 2)
#a, r1 = divmod(a, 2)
#print(a)
#print(r5, r4, r3, r2, r1))

b23 = ''
a = 23
while a != 0:
    a, r = divmod(a, 2)
    b23 = str(r) + b23
print(b23)
