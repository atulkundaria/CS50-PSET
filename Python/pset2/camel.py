camel_case = input("camelCase: ").strip()

for l in camel_case:
	if l.isupper():
		newn = "_" + l.lower()
		l = newn
	print(l, end="")
