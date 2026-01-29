# # names = []

# # for i in range(3):
# #     names.append(input("whats your name"))
# # for name in names:
# #     print(f"hello, {name}")    

# name = input("whats your name?: ") 

# file = open("names.txt", "w") # open file in write mode
# file.write(f"\n{name}")
# file.close()


# # file = open("names.txt", "a") # open file in write mode
# # file.write(f"\n{name}")
# # file.close()

# with open("example.txt", "w") as f:
#     f.write("Hello, world!")

# Appends names to a list for sorting
# name = []

# with open("names.txt") as f:
#     for line in f:
#         name.append(line.rstrip())
        
# for name in sorted(name):
#     print(f"hello, {name}")
        
with open("temp.csv", "w") as f:
    f.write("hello, world\n")