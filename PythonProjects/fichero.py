import os

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
    print('archivo borrado')
else:
    print('no hay archivo')

if os.path.exists('micarpeta'):
    os.rmdir('micarpeta')
    print('carpeta borrada')
else:
    print('no existe esa carpeta')
