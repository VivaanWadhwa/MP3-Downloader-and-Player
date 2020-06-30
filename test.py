import numpy
size,l,lFinal = int(input()),[],[]
for x in range(size):
    numb=int(input())
    l.append(numb)
for x in range(len(l)):
    s=numpy.prod(l)
    lFinal.append(s/l[x])
print (lFinal)
    

