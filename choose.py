
def factorial(n):
	if n > 1:
		return n*factorial(n-1)
	else: 
		return n
a= int (input('input the number of things you want to choose from, end with enter\n'))
b= int (input('input how many things you want to choose, end with enter\n'))

print('you got '+str(int(factorial(a)/factorial(b)/factorial(a-b)))+' possibilities')