def add_break():
    print("\n====================\n")

# Learning tuples!

# https://docs.python.org/3/tutorial/datastructures.html

###############################################################################
# TUPLES

# A tuple is sequence data type (others being lists and strings)

########################
# Example: Basic tuple 
########################

print("BASIC TUPLE\n")

a = 1234, 4312, "hello"
print(a) # On output, tuples are always in parentheses

add_break()

#########################
# Example: Nested tuples
#########################

print("NESTED TUPLE\n")

b = a, 1, 2, 3, 4, 5
print(b)

add_break()


#####################################
# Did you know? Tuples are immutable
#####################################

print("TUPLES ARE IMMUTABLE\n")

c = 3, 2, 1, 8, 9
# c[0] = 2
# Will result in an error
#   "TypeError: 'tuple' object does not support item assignment"
# This is because tuples are immutable, meaning the values are fixed and 
# cannot be altered

# However, you can add mutable objects to tuples
print("BUT YOU CAN HAVE MUTABLE OBJECTS IN TUPLES\n")

d = [9, 8, 7, 6]
print("array d:", d, sep=" ", end="\n\n")

e = d, (1, 2, 3)
print("tuple e with d as first element:", e, sep="", end="\n\n")

d[0] = 1
print("d and e again after changing first element of d\n")
print("d:", d, sep=" ")
print("e:", e, sep=" ")

add_break()


###############################################################################

