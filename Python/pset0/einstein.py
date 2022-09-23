def main():
	m = int(input("m: "))
	E = einstein(m)
	print(E)


def einstein(n):
	calc = n * pow(300000000, 2)
	return calc


main()
