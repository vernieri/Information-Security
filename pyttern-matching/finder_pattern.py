def starter():
	arq_name = raw_input("Manda ai o nome do arquivo que esta os patterns: ")
	f = open(arq_name, 'r')
	s = f.read()

	number = raw_input("Passa o Pattern: ")
	finder(s, number)
	f.close()
