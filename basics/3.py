#Validates email address by checking for @

email = input("What is your email address? ").strip()

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")
    
username,domain = email.split("@")

# if username and "." in domain:
#     print("Valid email")
# else:
#     print("Invalid email")   

if username and domain.endswith(".com"): #Checks if email ends with .com
    print("Valid email")
else:
    print("Invalid email")
    
    