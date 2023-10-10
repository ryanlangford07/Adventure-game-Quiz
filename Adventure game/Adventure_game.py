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
print("Question 3. What can someone do if they steal your identity")
print("1. Earn lots of money and leave it in your bank account")
print("2. Try to give you all the credit for their hard work")
print("3. Try access your bank and set up a loan in your name")
answer = input()
if answer == "3":
    print("Correct")
    print(f"You have {lives} lives")
else:
    print("incorrect")
    lives -=1
    print(f"You have {lives} lives")
print("Question 4. What term describes winding someone up online?")
print("1. Posting")
print("2. Trolling")
print("3. Phishing")
answer = input()
if answer == "2":
    print("Correct")
    print(f"You have {lives} lives")
else:
    print("incorrect")
    lives -=1
    print(f"You have {lives} lives")
print("Question 5. What software can you use to avoid getting a virus?")
print("1. Disk clean up software")
print("2. Firewall software")
print("3. Anti-virus Software")
answer = input()
if answer == "3":
    print("Correct")
    print(f"You have {lives} lives")
else:
    print("incorrect")
    lives -=1
    print(f"You have {lives} lives")
print("Question 6. What name would you give to an email attachment that may harm your computer??")
print("1. Phishing")
print("2. Spam")
print("3. Malware")
answer = input()
if answer == "3":
    print("Correct")
    print(f"You have {lives} lives")
else:
    print("incorrect")
    lives -=1
    print(f"You have {lives} lives")