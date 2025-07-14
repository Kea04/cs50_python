filename = input(str("Filename: ").strip())
filename_lower = filename.lower()

filename_index = filename_lower[-3:]

if filename_index == "gif":
    print("image/gif")
elif filename_index == "jpg":
    print("image/jpg")
elif filename_index == "peg":
    print("image/jpeg")
elif filename_index == "png":
    print("image/png")
elif filename_index == "pdf":
    print("application/pdf")
elif filename_index == "txt":
    print("text/txt")
elif filename_index == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
