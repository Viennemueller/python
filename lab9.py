list_1 = [2, 1, 0, 5, 2]
list_2 = ["foo", "baz", "bar"]
print(list_1*2)
print(list_1[:3])
list_1.remove(2)
print(list_1)
list_2.sort()
print(list_2)
list_2.append("blah")
print(list_2)


id_gpa = {1234: 3.9, 2319: 2.5, 9001: 3.4, 8475: 1.99}

# Print the GPA associated with ID 2319
print(id_gpa[2319])

# Print the keys (student IDs)
print(id_gpa.keys())

# Update the GPA for ID 8475 to 2.8
id_gpa[8475] = 2.8
print(id_gpa)

# Update the GPA for ID 2319 to 2.8
id_gpa[2319] = 2.8
print(id_gpa)

# Try to access the GPA for ID 3702, which is not in the dictionary
print(id_gpa.get(3702, "ID 3702 not found"))
