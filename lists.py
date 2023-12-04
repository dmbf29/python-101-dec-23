beatles = ["john", "ringo", "seb"]
# index      0        1       2

# CRUD

# Create
# list.append('new value')
beatles.append('paul')

# Read
# list[index]
# print(beatles[0])
# print(beatles[-1])
# print(beatles[4]) # Error
# print(len(beatles))
# index = 1
# print(beatles[index:])

# Update
# list[index] = 'new_value'
beatles[2] = 'george'

# Delete
# del list[index]
# list.remove('value')
del beatles[0]
sorted = sorted(beatles)
beatles.remove('ringo')
print(sorted)
print(beatles)

# function / methods


# to sort an array and the original
beatles.sort()

# to sort the array and create a new copy of it
sorted(beatles)
