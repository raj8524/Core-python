d=dict()
l1='aaabcaaddee'
print(l1[::3])
for i in zip(*[iter(l1)]*3):

    print(i)
    print(''.join([d.setdefault(c,c) for c in i if c not in d]))
print(d)
