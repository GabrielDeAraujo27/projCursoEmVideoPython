from random import randint
from sys import getsizeof

numAleat=(randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9),)
print(numAleat[0:])
numOrden=sorted(numAleat)
print(numOrden[0])
##numFim= len(numAleat)
print(numOrden[len(numAleat)-1])