checklist = list()
checklist.append('Blue')
#print(checklist)
checklist.append('Orange')
#print(checklist)

# CREATEs
def create(item):
    checklist.append(item)

# READ
def read(index):
    if index >= 0 and index < len(checklist):
        return checklist[index]
    else:
        print("invalid index")

# UPDATE
def update(index, item):
    if index >= 0 and index < len(checklist):
        checklist[index] = item
    else:
        print("invalid index")
    

# DESTROY
def destroy(index):
    if index >= 0 and index < len(checklist):
        checklist.pop(index)
    else:
        print("invalid index")

#List items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#Mark completed
def mark_completed(index):
    if index >= 0 and index < len(checklist):
        current_item = checklist[index]
        if "√" in current_item:
            return ""
        else:
            update(index, "√" + checklist[index])
            return checklist[index]
    else:
        print("invalid index")

#User Input
def user_input(prompt):
    user_input = input(prompt)
    return user_input


#Select
def select(function_code):
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input Item: ")
        create(input_item)
        return True

    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number? ")
        item = read(int(item_index))
        print(item)
        return True

    elif function_code == "P" or function_code == "p":
        list_all_items()
        return True

    elif function_code == "Q" or function_code == "q":
        return False

    elif function_code == "U" or function_code == "u":
        item_index = user_input("Index Number? ")
        new_item = user_input("Input Item:")
        update(item_index, new_item)
        return True

    elif function_code == "D" or function_code == "d":
        item_index = user_input("Index Number?")
        destroy(item_index)
        return True

    elif function_code == "M" or function_code == "m":
        item_index = user_input("Index number?")
        mark_completed(int(item_index))
        return True
    else:
        print("Unknown Option")


  
running = True
while running:
    selection = user_input("Press C to add to the list, R to read from the list, \n U to update the list, D to delete something from the list, \n  P to display the list, M to mark an item as complete, and Q to exit \n")
    running = select(selection)





# TEST
#def test():
    #Add testing code here
    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(0)

    # print(read(0))
    # print(read(1))
    # print(mark_completed(0)) 
    # select("C")
    # list_all_items()
    # select("R")
    # list_all_items()