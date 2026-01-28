import re 

email = input("Enter your email address: ").strip()

if re.search(r"^[\w.-]+@[\w.-]+\.(edu|com|org)$", email): 
    print("Valid email")
else:
    print("Invalid email")