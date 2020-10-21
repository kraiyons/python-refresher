l = ["Bob", "Rolf", "Anne"]

t = ("Bob", "Rolf", "Anne")
# Can't modify a tuple

s = {"Bob", "Rolf", "Anne"}
# Can't have duplicate elements
# Order is not guaranteed


l.append("Smith")

# t.append("Smith")
# Tuples cannot be modified

s.add("Smith")
s.add("Bob")
# Only 1 bob will be printed, curiously, first bob was deleted

print(l)
print(t)
print(s)