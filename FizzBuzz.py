inputString = int(raw_input("Enter a number: "))

if inputString % 5 == 0 and inputString % 3 == 0:
	print "Fizz Buzz"
elif inputString % 3 == 0:
	print 'Fizz'
elif inputString % 5 == 0:
	print 'Buzz'
else:
	print "Not divisible by 3, 5 or 15"
