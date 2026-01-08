# print -> variable length 
# * -> variable length arguments
# (different objects)  (sepearator used to separate objects)
#seperator works on objects
#end works wih print statement
#  screen -> buffer -> console  (interpreter)
# using flush we skip the buffer and directly print to the console (after 3.10 version) it has been introduced
#memory assigning --> reason for dynamic data type

# print("Hello", "world!", 123, 45.67, sep=" | ")
# print("Hello", end="")
# print(10)
# print(20, end="--")


# a = open("sample.txt") #opening file
# a = open("sample.txt", 'w')  #scope

# #write function
# a.write("Hello world\n")
# a.write(10)


"""
print("hello", flush = True)
print("hello")

print(1,2,3, flush=True)
print(1,2,3)
"""


#KGM Pattern printing
# *  *
# * *
# **
# * *
# *  *

# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == i or j == n - i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("*")


# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n/2 or () :
#             print("*", end="")
#         else:
#             print(" ") 

