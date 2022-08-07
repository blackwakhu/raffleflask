import random
# uses the python random function to get the value of the respective tickets

def first(fbet):
	# this is for the first ticket whose max is 10
	true_val = random.randint(0, 10)
	if true_val == int(fbet):
		return 100, 'you won 100'
	else:
		return 0, 'you lost'

def second(sbet):
	# second ticket whose max is 100
	true_val = random.randint(0, 100)
	if true_val == int(sbet):
		return 1000, 'you won 1000'
	else:
		return 0, 'you lost'

def third(tbet):
	# third ticket whose max is 1000
	true_val = random.randint(0, 1000)
	if true_val == int(tbet):
		return 10000, 'you won 10000'
	else:
		return 0, 'you lost'

def bonus(bbet):
	# bonus ticket whose max is 10,000
	true_val = random.randint(0, 10000)
	if true_val == int(bbet):
		return 100000, 'you won 100000'
	else:
		return 0, 'you lost'