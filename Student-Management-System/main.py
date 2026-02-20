from database import create_table
from service import add_student,get_all_students

def main():
    create_table()

    print('''
        Welcome to Student Dashboard !
        Select your choice :-
        1. Add students data 
        2. View all data 
        3. Exit
''')
    while True:
        try:
            choice = int(input("Enter your choice"))

            if choice == 1 :
                name = input("Enter student name : ")
                marks = input('Enter student marks : ')
                
                message = add_student(name,marks)
                print(message)

            elif choice == 2:
                data = get_all_students()

                if isinstance(data,str):
                    print(data)
                else:
                    for student in data:
                        print(student["id"],student["name"],student["marks"])

            elif choice == 3 :
                print("Thank you !")
                break

            else:
                print("Enter valid choice")
        
        except ValueError:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()