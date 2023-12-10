''' CONCATENACION '''

cadena1 = 'Hola, '
cadena2 = '¿Cómo estás?\n'
resultado = cadena1 + cadena2
print(resultado)

cadena3 = 'Mi edad es '
edad1 = 25
resultado1 = cadena3 + str(edad1) + '\n'
print(resultado1.upper())

nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
edad = int(input('Edad: '))
# print('Hola, mi nombre es ' + nombre + ' ' + apellido + '\n')

''' F-STRINGS '''
saludo = f'Hola mi nombre es {nombre} {apellido} y tengo {edad} años\n'
print(saludo)

''' CONCATENAR CON LISTAS '''
numeros = [1,2,3,4,5]
resultado_lista = ''
for num in numeros:
    resultado_lista += str(num) + ' '
print(resultado_lista)

''' CONCATENACION CON JOIN '''
palabras = ['Hola','Mundo', 'Python']
frase = ' '.join(palabras)
print(frase)
