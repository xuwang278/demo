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
	print('added in the branch of new feature')
	print('added a new line in the branch of latest feature')
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
