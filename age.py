# This simple program can tell you if yuo are an adult or a child (or a boy)

name = input("Heyo! What's your name? ")
age = str(input("Hi {}, how old are you?".format(name)))

if (age < 18):
    print("You're underage !\n ")
    input("Press 'Enter' to close. ")

if (age > 18):
    print("Oh, Wow! You're an adult!\n ")
    input("Press 'Enter' to close. ")

if (age < 10):
    print("Hi little child!\n ")
    input("Press 'Enter' to close. ")
