import datetime
from datetime import date
import _datetime
name = input("What is your name?")
birthMonth = int(input("What is your birth month?"))
if birthMonth == datetime.date.today().month:
    print("Happy Birth Month!")
print("Hello " + name + ".")
print("Your name has " + str(len(name)) + " letters in it.")
