import numpy as np

np.set_printoptions(sign=' ')


arr = np.array(input().split(),float)

def fcd(array):


   print (np.floor(array))
   print (np.ceil(array))
   print (np.rint(array))


fcd(arr)
