def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


def is_valid(num):
	lnum = len(num)
	# “All vanity plates must start with at least two letters.”
	# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
	if lnum < 2 or lnum > 6:
		return False

	if not num[0].isalpha() and not num[1].isalpha():
		return False
	# “No periods, spaces, or punctuation marks are allowed.”
	if not num.isalnum():
		return False
	# “Numbers cannot be used in the middle of a plate; they must come at the end.
	# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
	# The first number used cannot be a ‘0’.”
	i = 0
	while i < lnum:
		if not num[i].isalpha():
			if num[i] == "0":
				return False
			else:
				break
		i += 1

	for x in num:
		if x.isdigit():
			i = num.index(x)
			if not num[i:].isdigit():
				return False
	return True


main()
