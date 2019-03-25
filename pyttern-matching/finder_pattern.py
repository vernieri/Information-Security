def starter():
	arq_name = raw_input("Manda ai o nome do arquivo que esta os patterns: ")
	f = open(arq_name, 'r')
	s = f.read()

	number = raw_input("Passa o Pattern: ")
	finder(s, number)
	f.close()
	
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
