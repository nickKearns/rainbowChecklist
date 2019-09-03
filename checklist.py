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
    for list_item in checklist:
        print(list_item)



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
    



test()
