from os import name, system

def cross_clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')