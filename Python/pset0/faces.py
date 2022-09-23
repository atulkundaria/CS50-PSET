def main():
	sentence = input("Here: ")
	sentence = convert(sentence)
	print(sentence)


def convert(sen):
	sen = sen.replace(":)", "🙂")
	sen = sen.replace(":(", "🙁")
	return sen


main()
