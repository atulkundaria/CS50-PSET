file_name = input("File Name: ").strip().lower()

if file_name.endswith("jpg") or file_name.endswith("jpeg"):
	print("image/jpeg")
elif file_name.endswith("gif") or file_name.endswith("png"):
	f = file_name.split(".")
	print(f"image/{f[-1]}")
elif file_name.endswith("pdf") or file_name.endswith("zip"):
	f = file_name.split(".")
	print(f"application/{f[-1]}")
elif file_name.endswith("txt"):
	print("text/plain")
else:
	print("application/octet-stream")


