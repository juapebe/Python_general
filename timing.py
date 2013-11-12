#This function calculates, for a given function and its (single) argument, how long it takes to run, and prints the result.
#Extracted from the Object Oriented Programming course at UCSF. 2013. Exercise 4.1

def timing(func, argument, repeat=1000):
	import time
	total = 0.0
	for i in range(repeat):
		start = time.time()
		func(argument)
		total += time.time() - start
	print "Average time (ms):", total / repeat * 1000.0

#THese two lines are from the course exercise description.
#timing(has_dups, test_list)
#timing(has_dups_list, test_list)