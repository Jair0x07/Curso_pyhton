def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

#LINEA 4= CUATRO ARGUMENTOS
#LINEA 5= TRES ARGUMENTOS
#LINEA 6= UN ARGUMENTO
#LINEA 7= DOS ARGUMENTOS

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('azul', 'rojo')#ya antes puesto los argumentos en la lista que hicimos los tomamos para imprimirlos.

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos números es:', resultado)

suma(3, 9, 81, 57, 104, 250)