inputString = int(raw_input("Enter a number: "))

if inputString % 3 == 0:
	print 'Fizz'
elif inputString % 5 == 0:
	print 'Buzz'
elif inputString % 15 == 0:
	print 'FizzBuzz'
else:
	print "Not divisible by 3, 5 or 15"