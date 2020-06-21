import numpy

n = input()
dat=[]
for i in range(0,int(n)):
    dat.append(input().split(' '))

data=numpy.array(dat)

data=data.astype('float')

print(round(numpy.linalg.det(data),2))

