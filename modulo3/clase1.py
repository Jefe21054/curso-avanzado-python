cadena = 'Python es genial'
caracter = cadena[7:9]
print(caracter)
caracter2 = cadena[0:10:2]
print(caracter2)
reversa = cadena[::-1]
print(reversa)

lenguajes_programacion = 'python php go c# javascript java'
lista_lenguajes = lenguajes_programacion.split(' ')
print(lista_lenguajes)

print(lista_lenguajes[2:4])
print(lista_lenguajes[0:4:2])

email = 'usuario@ed.team'
dominio = email[email.index('@') + 1:]
print(dominio)
