import sys

def default():
	print('Hello')

def cow():
	print('cow')

def main():
	if sys.argv[1] == 'cow':
		cow()
	else:
		default()

if __name__ == '__main__':
	main()
