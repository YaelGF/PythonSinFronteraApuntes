w = open('chanchito.txt', 'w')
w.write('\nagregamos nuevo texto')

w.close()

c = open('chanchito.txt' ,'a')
c.write('\nagregaremos una nueva linea a nuestro archivo')

c.close()

x = open('chanchito.txt','r')
print(x.read())

x.close()
