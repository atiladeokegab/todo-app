# function to reduce redundances
FILEPATH = "todos.txt"
#atilade

def get_todos(filepath = FILEPATH):
    """
    Redad a text file and return the list of
    to do items.
    :param filepath: todos.txt
    :return: todos_local
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#code below provides an explanation for the coded functions
#print(help(get_todos))
#print(help(write_todos)

def write_todos(todos_arg ,filepath = FILEPATH):
    """
    write the to-do items list into the text file
    :param todos_arg: list of todos
    :param filepath: location of filex
    :return: none
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#print("i am outside")
if __name__ == "__main__":
    """
    if __name__ == "__main__":
    this is a line of code that helps to differentiate the direct running of the code 
    and the indirect running of a code 
    for example in the main_todo_list file 
    when it is run the file code under the 
    if __name__ == "__main__":
    is not ran 
    but when the functions.py file 
    is run the code works
    """
    print("This is from the functions.py file")
    print(get_todos())