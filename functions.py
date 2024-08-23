FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """De help voor get_todos:
        Het is een functie die een lijstje regelt
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath="todos.txt"):
    """Deze doet schrijven :D"""
    with open(filepath, 'w') as file_loca:
        file_loca.writelines(todos_local)
        # geen return want is niet nodig, deze functie past de txt aan


print("Ik moest hier wat zetten")
if __name__ == "__main__":
    print("__main__ uitvoering")
