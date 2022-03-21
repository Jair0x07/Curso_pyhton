x = 0 #valor inicial

# while se ejecuta hasta menor o igual que 30
while x <= 30:
	x += 1  # incrementos de 1

	# if para saltar ejecuciones del bucle
	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor ', x)
		continue

	# if para romper la ejecución del bucle
	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break

	# imprime los resultados que no se corresponden a ninguno de los if
	print(x)





