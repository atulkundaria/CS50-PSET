greeting = input("Greeting: ").strip().lower()
if greeting.startswith("hello"):
	print("$0")
elif "how" in greeting.split():
	print("$20")
else:
	print("$100")
