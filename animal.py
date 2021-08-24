import sys

def default():
	print('Hello')

def cat():
	print('Meow')

def dog():
	print('Woof')

def cow():
	print('cow')

def main():
	if sys.argv[1] == 'dog':
		dog()
	elif sys.argv[1] == 'cat':
		cat()
	elif sys.argv[1] == 'cow':
		cow()
	else:
		default()
		
if __name__ == '__main__':
	main()
