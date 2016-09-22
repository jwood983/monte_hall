from random import randrange

def monty_hall_guess():
	"""
		Returns a random integer between 1-3
	"""
	return randrange(1,4)

def prize_behind():
	"""
		The prize is behind *this door
	"""
	return randrange(1,4)

def show_bad(spot, guess):
	"""
		Shows a bad door, given the prize spot & guess
	"""
	if spot==1:
		return 2 if guess==3 else 3
	if spot==2:
		return 1 if guess==3 else 3
	if spot==3:
		return 1 if guess==2 else 2

def new_guess(guess, bad):
	"""
		Given the original guess and the bad door, return the alternative
	"""
	if bad==1:
		return 3 if guess==2 else 2
	if bad==2:
		return 1 if guess==3 else 3
	if bad==3:
		return 2 if guess==1 else 1

switching = 0.0
staying   = 0.0
niters    = 5000
for i in xrange(niters):
	# set the location of the prize
	spot  = prize_behind()
	# make a guess
	guess = monty_hall_guess()
	# show the bad door!
	bad   = show_bad(spot, guess)
	#~ print 'door=%d, guess=%d, revealed=%d, ' % (spot, guess, bad),
	
	# handle staying
	staying += 1.0 if guess==spot else 0.0
	#~ print 'stay win = %s' % ("yes" if guess==spot else "no "),
	
	# handle switching
	guess = new_guess(guess, bad)
	switching += 1.0 if guess==spot else 0.0
	#~ print 'new guess=%d, switch win = %s' % (guess, "yes" if guess==spot else "no")
	

print 'After %d iterations, we have some results:' % niters
print '\tStaying had a success rate of %f' % (staying / niters)
print '\tSwitching had a success rate of %f' % (switching / niters)

