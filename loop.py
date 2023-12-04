beatles = ["john", "ringo", "george", "paul"]

# for parameter in collection:
  # doing whatever code we want

# exclusive -> doesnt include the last number
counter = 1
for beatle in beatles:
    print(f"{counter}.) {beatle}")
    counter = counter + 1


# counter = 1
# for index, beatle in enumerate(beatles):
#     print(f"{index + 1}.) {beatle}")


upcased_name = []
for beatle in beatles:
    upcased_name.append(beatle.upper())

# This is the same as above, just in one line
upcased_name = [beatle.upper() for beatle in beatles]

print(upcased_name)
