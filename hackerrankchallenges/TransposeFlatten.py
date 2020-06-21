import numpy

n,m =map(int,input().split())

array= numpy.array([input().strip().split() for i in range(0,n)],int)

print(numpy.transpose(array))
print(array.flatten())
