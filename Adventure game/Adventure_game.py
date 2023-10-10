lives = 3
print(f"You have {lives} lives")
print("Hello and welcome to this E-Safety quiz.")
print("Question 1. What one of these is a form of personal information?")
print("1. Date of birth")
print("2. Gender")
print("3. Online usernames")
answer = input()
if answer == "1":
    print("Correct")
    print(f"You have {lives} lives")
else:
    print("incorrect")
    lives -=1
    print(f"You have {lives} lives")
print("Question 2. What can you do to get less email spam?")
print("1. Always tick dont send updates")
print("2. Change your email address every six months")
print("3. Never use your email adress")
answer = input()
if answer == "1":
    print("Correct")
    print(f"You have {lives} lives")
else:
    print("incorrect")
    lives -=1
    print(f"You have {lives} lives")

