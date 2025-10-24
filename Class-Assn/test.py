# Jacob Cardon
# CS1400 - MWF - 8:30am

# id.py

print("These ID number are hard to read; focus on the last 4 digits")
print("id(7) is    ", id(7))
print("id(8) is    ", id(8))

a = 7
b = 8
seven = 7

print("\n'a' and 'seven' share the same ID with id(7) above")
print("id(a) is    ", id(a))
print("id(b) is    ", id(b))
print("id(seven) is", id(seven))


print("\nIncrementing seven...\n")
seven += 1


print("now 'b' and 'seven' have the same ID")
print("id(a) is    ", id(a))
print("id(b) is    ", id(b))
print("id(seven) is", id(seven))

print("\nIdentical integers share an ID, but identical lists and tuples do not")
l0 = [0, 1, 2, 3]
l1 = [0, 1, 2, 3]
print("id(l0) is   ", id(l0), "and the object looks like this:", l0)
print("id(l1) is   ", id(l1), "and the object looks like this:", l1)
print("l0 == l1 is ", l0 == l1)
print("l0 is l1 is ", l0 is l1)

print("\nAssigning l0 = l1...\n")
l0 = l1
print("l0 == l1 is ", l0 == l1)
print("l0 is l1 is ", l0 is l1)

print("\nAssigning l0[1] = 'hello world'...\n")
l0[1] = 'hello world'
print("Now the l0 object looks like this:", l0)
print("And the l1 object looks like this:", l1)
print("l0 == l1 is ", l0 == l1)
print("l0 is l1 is ", l0 is l1)

print("\nMaking tuples out of l0...\n")
t0 = tuple(l0)
t1 = tuple(l0)
print("id(t0) is   ", id(t0), "and the object looks like this:", t0)
print("id(t1) is   ", id(t1), "and the object looks like this:", t1)
print("t0 == t1 is ", t0 == t1)
print("t0 is t1 is ", t0 is t1)
