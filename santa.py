from sys import argv

script, user_name = argv
promt = '> '

print(f"Hi {user_name}, Im the {script} talking.")
print("I'd like to ask you a few questions.")
print(f"Do you believe in me {user_name}?")
likes = input(promt)

print(f"Where do you live {user_name}?")
lives = input(promt)

print("Wow I've been there alot of times!")

print(f"what do you want for christmas {user_name}?")
christmas = input(promt)

print("And i know you have a brother whats his name?")
brother = input(promt)

print(f"""
You live in {lives}. I know where that is.
And you have a brother {brother}.
Ok ill do my best to ensure you have a great christmas!
Merry Christmas!!

HO HO HO
Bye
""")
