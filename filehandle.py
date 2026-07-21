with open("file1.txt","w") as file:
    file.write("hello world")
with open("file1.txt","r") as file:
    print(file.read())
with open("file.txt","a") as file:
    file.write("python programming")
    