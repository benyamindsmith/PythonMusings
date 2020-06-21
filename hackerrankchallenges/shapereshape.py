import numpy

n = input().split(' ')

data = []

for i in n:
    data.append(int(i))

data=numpy.array(data)

print(numpy.reshape(data,(3,3)))
