def main():
	print("Amount Due: 50")

	due = 50
	due_calc(due)


def due_calc(changeowned):
	while changeowned > 0:
		coin = int(input("Insert Coin: "))

		if coin == 25 or coin == 10 or coin == 5:
			changeowned -= coin
			if changeowned > 0:
				print(f"Amount Due: {changeowned}")
			else:
				print("Change Owned", abs(changeowned))
		else:
			print(50)


main()
