def multi_table(a):

	for i  in range(1, 11):
		print('{0} x {1} = {2}'.format(a, i, a*i))
		
		
		
if __name__ == '__main__':
	a = input('72: ')
	multi_table(float(a))
