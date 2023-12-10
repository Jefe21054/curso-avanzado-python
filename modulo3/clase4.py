name = 'Ivan'
age = 25
print(f'Mi nombre es {name} y tengo {age} años.')
print('Mi nombre es {} y tengo {} años.'.format(name, age+10))

sql_insert = "insert into users(name,age) values('{}','{}')".format(name, age)
print(sql_insert)

print('Nombre: {1}, Edad: {0}'.format(age, name))

''' PRINT CON PARAMETROS '''
producto = 'Celular iPhone 12'
precio = 599.99

print('Producto: {prod}, Precio: {price}'.format(prod=producto, price=precio))

''' FORMATEO DE NUMEROS '''
numero = 12345.6889
print("{:.2f}".format(numero)) # Formato con 2 decimales
print("{:,}".format(numero))   # Formato con separadores de miles
print("{:e}".format(numero))   # Formato notacion cientifica

''' FORMATEO DE FECHAS '''
from datetime import datetime
ahora = datetime.now()
print('Fecha y hora: {:%Y/%m/%d %H:%M:%S}'.format(ahora))

''' ALINEACION Y RELLENO '''
number = 42
print("Numero: {:>10}".format(number)) # Da numero de espacios
print("Numero: {:0<5}".format(number)) # Rellena con ceros hasta cumplir 5 espacios a partir del numero
