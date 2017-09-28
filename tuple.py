tup = ()
tup1 = tuple()
tup2 = (0,1,2,3,4,5)
tup3 = tuple(tup2)

print(tup)
print(tup1)
print(tup2)
tup2 = tup2 + (6,7,8,9,10)
print(tup3)

print(len(tup2))

for i in tup2 :
    print i

    print 1 in tup2
    print(110 in tup2)