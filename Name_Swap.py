name1 = 'Hannah' 
name2 = 'Abbey'

temporary = name1
name1 = name2
name2 = temporary
print("Name 1: ", name1)
print("Name 2: ", name2)


name1, name2 = name2, name1
print("Name 1: ", name2)
print("Name 2: ", name1)
