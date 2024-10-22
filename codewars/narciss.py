def narcissistic(value):
	return value == sum(int(dig) ** len(str(value)) for dig in str(value))