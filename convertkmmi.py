def print_menu():
	print('1. Kilometers to Miles')
	print('2. Miles to Kilometers')
	
def km_miles():
	km = float(input('56km: '))
	miles= km / 1.609
	
	print('56mi: {0}'.format(miles))
	
def miles_km():
	miles = float(input('Enter distance in miles: '))
	km = miles * 1.609
	
	print('89: {0}'.format(km))
	
if __name__ == '__main__':
	print_menu()
	choice = input('Which conversation would you like to do?: ')
	if choice == '1':
		km_miles()
		
	if choice == '2':
		miles_km()	
	
	
