entrada = input('Introduce un color:\n')#entrada de datos para el usuario con input
colores = ('azul', 'rojo', 'amarillo', 'verde')#se crea la tupla

if entrada in colores[0]:#condicion (true) con la ubicacion en la tupla
	print('El color azul está admitido')
elif entrada in colores[1]:#condicion (true) con la ubicacion en la tupla
	print('El color rojo está admitido')
elif entrada in colores[2]:#condicion (true) con la ubicacion en la tupla
	print('El color amarillo está admitido')
elif entrada in colores[3]:#condicion (true) con la ubicacion en la tupla
	print('El color verde está admitido')
else:
	print('Color no admitido')#condicon (false)
