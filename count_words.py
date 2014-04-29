if __name__ == '__main__':
	inputstring = raw_input("Enter a sentence to count: \n") # Get input from user
	
	counts = [] # Declare empty array

	for i in inputstring:
		if i.isalnum() or i.isspace(): # if inputstring has a number or a space in it append to counts
			counts.append(i)
		else:
			counts.append(' ')
	new_input = "".join(counts)
	print len(new_input.split()) # Print length of counts
