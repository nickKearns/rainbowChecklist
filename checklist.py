checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)
# CREATEs
def create(item):
    checklist.append(item)
# READ
def read(index):
    if index > 0 and index < len(checklist):
        return checklist[index]
    else:
        return "Invalid index"
# UPDATE
def update(index, item):
    if index > 0 and index < len(checklist):
        checklist[index] = item
    else:
        print("Invalid index")
# DESTROY
def destroy(index):
    if index > 0 and index < len(checklist):
        checklist.pop(index)
    else:
        print("Invalid index")
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    if index > 0 and index < len(checklist):
        current_item = checklist[index]
        if "√" in current_item:
            return ""
        else:
            update(index, "√" + checklist[index])
            return checklist[index]
    else:
        print("Invalid index")

def select(function_code):
    if function_code == "C" or "c":
        input_item = user_input("Input Item: \n")
        create(input_item)
    elif function_code == "R" or "r":
        item_index = user_input("Index Number? \n")
        read(item_index)
    elif function_code == "P" or "p":
        list_all_items()
    elif function_code == "Q" or "q":
        return False
    elif function_code == "U" or "u":
        item_index = user_input("Index Number? \n")
        new_item = user_input("Input Item: \n")
        update(item_index, new_item)
    elif function_code == "f" or "f":
        item_index = user_input("Index Number? \n")
        destroy(item_index)
    else:
        print("Unknown Option")


        
def user_input(prompt):
    user_input = input(prompt)
    return user_input



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

running = True
while running:
    selection = user_input("Press C to add to the list, R to read from the list, \n P to display the list, and Q to stop exit \n")
    select(selection)
    if selection == "Q":
        running = select("Q")

