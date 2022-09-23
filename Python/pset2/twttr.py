twitter = input("Input: ")

vocal = ["A", "E", "I", "O", "U", "a", "e", "o", "u", "i"]

print("Output: ", end="")

for l in twitter:
	if l not in vocal:
		print(l, end="")
