import zipfile

filename = input("Path: ")

with zipfile.ZipFile(filename, "r") as z:
    z.extractall("")
