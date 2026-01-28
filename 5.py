# gets a number from the user

# x = int(input("Whats x?:"))
# print(f"x is {x}")
# while True:
#     try:
#         y = int(input("Whats y?: "))
    
#     except:
#         print("That is not a valid integer.")
#     else:
#         print(f"y is {y}")
#         break
    
# def main():
#     x = get_int()
#     print(f"x is {x}")
    
# def get_int():
#     while True:
#         try:
#             x = int(input("Whats x?: "))
#         except:
#             print("That is not a valid integer.")
#         else:
#             return x

# main()

def main():
    x = get_int()
    print(f"x is {x}")
    
def get_int():
    while True:
        try:
            return int(input("Whats x?: "))
        except:
            pass

main()    