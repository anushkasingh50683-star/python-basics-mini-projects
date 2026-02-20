from service import register_user
from database import create_table

def main():
    create_table()
   
    name = input("Enter you name: ")
    message = register_user(name)

    print(message)

if __name__ == "__main__":
    main()



'''
If you write main() directly at the bottom of your file without using if __name__ == "__main__":, then the function will execute every time the file is loaded by Python. This means it will run not only when you execute the file directly (for example, using python main.py), but also when another file imports it. Since importing a file causes Python to execute all top-level code inside it, calling main() without the guard makes the program start automatically during import. This is usually undesirable because importing a module should only make its functions available, not trigger the entire program. The if __name__ == "__main__": condition prevents this by ensuring that main() runs only when the file is executed directly, and not when it is imported into another file.
'''