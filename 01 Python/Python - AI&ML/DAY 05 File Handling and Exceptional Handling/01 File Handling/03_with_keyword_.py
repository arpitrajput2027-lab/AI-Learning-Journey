# By suing with keyword, we don't need to explicitly close the file.
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)