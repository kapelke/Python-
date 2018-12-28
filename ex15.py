from sys import argv # imports a module from the library

script, filename = argv #

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("type the file {filename}:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()
