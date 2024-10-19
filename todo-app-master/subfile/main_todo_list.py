# from functions import get_todos, write_todos
import functions
import time
import datetime

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is ", now )
print(f"it is now {now}")


print("this code is the backend code for my todolist app. this is just a beta")
while True:
    # this line gets the user's input and strips it of extra space elements and also converts it to lowercase
    # this is done to improve readability
    user_action = input("Type command with todo: ")
    user_action = user_action.strip()  # this method helps to remove excess space from the end of the string
    user_action = user_action.lower()  # this method helps to allow the user to enter any case and still get a result, e.g., add or ADD will yield the same output


    if user_action.startswith('add') :
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}:) {item}"
            print(row)
        print(f"you currently have {len(todos)} items to complete\n")
        print(f"number of items to be completed: {len(todos)}\n")
        print(todos)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])  # we do this to convert string to int
            print(number)
            number -= 1

            todos = functions.get_todos()
            print('Here are the existing todos:', todos)

            new_todo = input("enter new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid. Please enter the number of the thing to be edited e.g edit 1")
            continue

    elif user_action.startswith('complete'):
        if len(todos) == 0:
            print("list is empty")
            continue
        else:
            try:
                number = int(user_action[9:])

                todos = functions.get_todos()

                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                functions.write_todos(todos)

                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)
            except IndexError:
                print("this number does not exist")
                continue
            except ValueError:
                print("please enter a number after the command")
                continue

    elif user_action.startswith('exit'):
        break

    elif user_action.startswith('clear'):
        with open('todos.txt', 'w') as file:
            file.write('')
        print("Todo list cleared.")

    else:
        print("command is not valid")

print("BYE!")
