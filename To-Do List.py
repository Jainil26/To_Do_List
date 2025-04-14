todo_list = []

print("Welcome to the To-Do List!")
print("Enter the task and when you're finished type 'Done' ")
print("=======================")
while True:
    task = input("Enter the task : ")
    if task=='Done':
        break
    else:
        todo_list.append(task)
print("=======================")
print("Your amazing to-do list")
print("=======================")
for i in todo_list:
    print(i,end="\n")