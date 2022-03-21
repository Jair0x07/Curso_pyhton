edad = int(input('¿Cuál es tu edad?\n'))#almacena el dato que se va a utilizar para saber si es true or false
if edad <= 0:#condicion true
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:#condicionalrango
	print('Eres menor de edad.')
elif edad <=18 and edad <45:#condicional rango
	print('eres adulto')
elif edad <= 100:#condicional true
	print('Eres mayor de edad.')
elif edad <= 100 and edad <120:#condicional rango
	print('Eres muy viejito.')
else:  ##condicional false
	print('Edad no válida.')

