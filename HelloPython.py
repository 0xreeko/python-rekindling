name = input("What is your name? ")
age = input('How old are you? ')


if int(age) > 18:
    ageChecker = 'you are a young adult'
else:
    ageChecker = 'you are a young person'

print(f"Hello {name}, {ageChecker} that can code!")
