# lambda function as anonymous function

def greet(name, cb):
    print(f"Hello {name}")
    cb()

# def say_bye():
#     print("Byee!!!!")

# say_bye = lambda : print("Byee!!")

greet("John", lambda : print("Byee!!"))