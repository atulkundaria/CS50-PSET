def main():
	expression = input("Expression: ").strip()
	calc = calculation(expression)
	print(f"{calc:.1f}")


def calculation(exp):
	x, y, z = exp.split(" ")
	x = int(x)
	z = int(z)
	if y == "+":
		return x + z
	elif y == "*":
		return x * z
	elif y == "/":
		return x / z
	elif y == "-":
		return x - z


main()
