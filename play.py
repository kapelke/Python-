from sys import argv

script, user_name = argv
promt = '> '

print(f"Hi {user_name}, Im the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(promt)

print(f"Where do you live {user_name}?")
lives = input(promt)

print("what kind of computer do you have?")
computer = input(promt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Niice
""")
