import mmap
import os
import binascii

lista = []

arq = raw_input('Entre com o nome >_ ')
with open(arq,'rb') as f:
	content = f.read()
originalfileHexString = binascii.hexlify(content)
print (type(originalfileHexString))



file = open(arq,'a+')
m = mmap.mmap(file.fileno(),0)

#save
for x in range(0,m.size()):
	print(">>")
	lista.extend(m[x])

#lck
for x in range(0,m.size()):
	print("#")
	m[x] = '*'
arq1 = raw_input('>_ ')

#ulk
for x in range(0,m.size()):
	print("+")
	m[x]=lista[x]

m.close()
file.close()
base = os.path.splitext(arq)[0]
os.rename(arq,base+'.asadi')
print(lista)