with open('file.txt' 'a', encoding="utf-8") as f:
    f.write("\ntest")

with open('file.txt', 'r', encoding="utf-8") as f:
    content = f.read()
    print(content)
