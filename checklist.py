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
    return checklist[index]
# UPDATE
def update(index, item):
    checklist[index] = item
# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index + list_item))
        index += 1

def mark_completed(index):
    current_item = checklist[index]
    if "√" in current_item:
        return ""
    else:
        update(index, "√" + checklist[index])
        return checklist[index]

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input Item:")
        create(input_item)
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(item_index)
    elif function_code == "P":
        list_all_items()
    else:
        print("Unknown Option")


        
def user_input(prompt):
    user_input = input(prompt)
    return user_input



# TEST
def test():
    # Add testing code here
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(0)

    print(read(0))
    print(read(1))
    print(mark_completed(0))


    



test()
