import sys

def default():
	print('hello')

def cat():
	print('meow')

def dog():
	print('woof')

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
