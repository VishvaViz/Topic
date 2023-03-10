#Condition Statement program
age=19
if age>=18:
    print("you can vote")
else:
    print("youn can't vote")

#Even Number
number=int(input("enter the Number"))
if number%2==0:
    print("Even number")
else:
    print("Odd Number")

#Condintion Checking

username=str(input("Enter the Username"))
password=int(input("Enter the Password"))

#Database
db_username="Vishva"
db_password=1234
if username==db_username and password==db_password:
    print("Login Sucessfully")
else:
    print("Invalid Password")

 
 
#otp concept
import random

otp=random.randint(0000,9999)

print(otp)

#Captcha concept
import string


captcha=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=5))

print(captcha)
