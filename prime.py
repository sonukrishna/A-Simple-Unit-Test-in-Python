
def is_prime(n):
    """checks the given nuber is prime or not """
    if n in (0, 1):
        return False
    for i in range(2, n):
	if n % i == 0:
	    return False
    return True

def print_next_prime(n):
    """print the closest prime larger than given """
    index = n
    while 1:
        index += 1
	if is_prime(index):
	    print index

#num = 17
#print is_prime(num)
#print_next_prime(num)
