import random
otp=random.randint(1000,2000)
print(otp)
print("Enter The Otp Which Got in Message Box")
otp_user=int(input())
if otp==otp_user:
    print("otp Varification successfull" )
else:
    print("Please Enter Correct Otp")