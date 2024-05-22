s = "Hello Jello"
# s[0] = "J" # will give an error, as strings are immutable

# But if you convert s to a list, you can change items in that list
s_list = list(s)
s_list[1] = "a"
new_s = "".join(s_list)
print(s, s_list, new_s, sep = "\n")

# Another way: slice the string and join it back
sliced_s = s[:1] + "u" + s[2:]
print(sliced_s)

