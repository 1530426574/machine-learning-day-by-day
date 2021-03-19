from numpy import tile

a = tile([0,1,2],(2,3,2))
print(a)
print('++++++++++++++++++++')
a = tile([0,1,2],(3,3,2))
print(a)
print('++++++++++++++++++++')
a = tile([0,1,2],(4,3,2))
print(a)

print('++++++++++++++++++++')
a = tile([0,1,2],(4,3,2))
print(a)
print('++++++++++++++++++++')
a = tile([0,1,2],(4,1,1))
print(a)