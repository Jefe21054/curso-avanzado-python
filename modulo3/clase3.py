texto = '''
Python es un lenguaje de alto nivel de programación 
interpretado cuya filosofía hace hincapié en la 
legibilidad de su código, se utiliza para desarrollar 
aplicaciones de todo tipo, por ejemplo: Instagram, 
Netflix, Spotify, Panda3D, entre otros. Se trata de 
un lenguaje de programación multiparadigma, ya que 
soporta parcialmente la orientación a objetos, 
programación imperativa y, en menor medida, 
programación funcional. Es un lenguaje interpretado, 
dinámico y multiplataforma.

Administrado por Python Software Foundation, posee 
una licencia de código abierto, denominada Python 
Software Foundation License. Python se clasifica 
constantemente como uno de los lenguajes de 
programación más populares.
'''
palabra_busqueda = input('Ingrese la palabra a buscar: ')
indice = texto.find(palabra_busqueda)

if(indice != -1):
    print(f'{palabra_busqueda} se encontro en el indice {indice}')
    total_encontrados = texto.count(palabra_busqueda)
    print(f'{palabra_busqueda} aparece {total_encontrados} veces')
else:
    print('No se encontro la palabra a buscar')

nuevo_texto = texto.replace('Python','python')
texto_una_sola_vez = texto.replace('Python','python',1)
