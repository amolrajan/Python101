@profile
def main():
	num = 50000000
	s=0;
	for i in xrange(num):
		s = s + i
	return
@profile
def sub():
	num = 50000000
	s = 0
	for i in xrange(num):
		s = s+i
	return

main()
sub()
