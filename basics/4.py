import re 

# email = input("Enter your email address: ").strip()

# if re.search(r"^\w+@\w+\.(edu|com|org)$", email,re.IGNORECASE): 
#     print("Valid email")
# else:
#     print("Invalid email")
    
mobile = input("Enter your mobile number: ").strip()

if re.search(r"^\d{10}",mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
    
