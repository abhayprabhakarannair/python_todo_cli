# Declare a list to store todos
todo_list = []

# Count initialized with 1 as a starting point
count = 1

# Do this code repeatedly until count reaches 5
while count <= 5:
    # Get input from user
    todo = input("Enter a todo: ")
    # Capitalize the entered todo_item
    capitalized_todo = todo.capitalize()
    # Add to the existing list
    todo_list.append(capitalized_todo)
    # Print list data
    print(todo_list)
    # Increment count
    count = count + 1

# Should have only 5 items
print("You entered " + str(len(todo_list)) + " todo items")

def get_ordinal(number: int):
    ordinal_val: str
    if number == 1:
        ordinal_val = str(1) + 'st'
    elif number == 2:
        ordinal_val = str(2) + 'nd'
    elif number == 3:
        ordinal_val = str(3) + 'rd'
    else:
        ordinal_val = str(number) + 'th'

    return ordinal_val


# Should out put all items one by one.
for index, todo in enumerate(todo_list):
    print("The " + get_ordinal(index + 1) + " todo item is " + todo)


