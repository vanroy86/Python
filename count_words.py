if __name__ == '__main__':
	inputstring = raw_input("Enter a sentence to count: \n")
	words = inputstring.split()

	counts = []

	for i in inputstring:
		if i.isalnum() or i.isspace():
			counts.append(i)
		else:
			counts.append(' ')
	new_input = "".join(counts)
	print len(new_input.split())
