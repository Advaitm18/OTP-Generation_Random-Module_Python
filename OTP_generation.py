import math, random
#import pywhatkit


print(("USER VERIFICATION").center(50))
name = input("Enter the Name: ")
phno = int(input("Enter the Phone No. "))
mailid = input("Enter the Email-ID: ")
           
characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
OTP = "" 
size=5
length = len(characters)
for i in range(size) : 
  OTP+= characters[math.floor(random.random() * length)]

message = f"\nHello {name} ! {OTP} is your One Time Password (OTP) for the User Verification"
print(message)
#pywhatkit.sendwhatmsg_instantly(phno, message)

while True:
  otp = input("\nEnter the Valid OTP: ")
  print("-----------------------------------------------------")
  if otp == OTP:
      print("Verification Successful")
      break
  else:
      print("Please, Recheck the entered OTP")
