#Some imports here

def starter():
	value = raw_input('Quantidade: ')
	loop(int(value))

def loop(value):
	lista = []
	i = 1
	while i <= value:
		
		hexa(i, lista)
		s = ''.join(lista)

		
		i += 1

	
	print(s)
	f = open('pattern.txt', 'w')
	f.write(s)
	f.close
	op = raw_input('Deseja continuar ou deseja sair<s/n>? ') #I might create a method just for it...
	if op=='s':
		number = raw_input("Digite o valor que deseja encontrar: ")
		finder(s, number)
	else:
		exit()

def hexa(i, lista):
	#Transforma em Hexa
	hexd = hex(i)
	str(hexd)
	lista.append(hexd)
		
starter()		
