#Password Generator

import random
import string
print("Welcome to the password generator")

def pas():
  length = int(input("Enter the length of the password: "))    
  lowerD=string.ascii_lowercase
  upperD=string.ascii_uppercase
  digitD=string.digits
  specialD=string.punctuation
  combine=lowerD+upperD+digitD+specialD
  if(length>=0):
    a=random.sample(combine,length)
    password="".join(a)
    print("Generated password:",password)
    response = input("Do you want to continue? (y/n): ")
    if response == 'y':
      return pas()
    elif response == 'n':
      print("Exiting the password generator. Goodbye!")
    else:
      print("Invalid input. Exiting the password generator.")
  else:
    print("OOPS! Invalid input")
    return pas()

pas()
