from service import register_user
from database import create_table

def main():
    create_table()

    name = input("Enter you name: ")
    message = register_user(name)

    print(message)

if __name__ == "__main__":
    main()