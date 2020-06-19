import numpy


def arrays(arr):
    new_array = numpy.asfarray(arr)

    return new_array[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
