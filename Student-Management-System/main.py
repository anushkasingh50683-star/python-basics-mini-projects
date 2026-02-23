from database import create_table
from service import add_student,get_all_students,update_student_data,delete_student_data

def main():
    create_table()

    print('''
        Welcome to Student Dashboard !
        Select your choice :-
        1. Add students data 
        2. View all data 
        3. Update student name or marks 
        4. Delete student data
        5. Exit
''')
    while True:
        try:
            choice = int(input("Enter your choice : "))

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
                id = input("Enter student id = ")
                new_name = input("Enter updated name = ")
                new_marks = input("Enter updated marks = ")

                updated = update_student_data(id,new_name,new_marks)
                print(updated)

            elif choice == 4:
                id = input("Enter student id = ")

                confirm = input("Are you sure to delete ? (y/n)").lower()
                if confirm == 'y' or confirm == 'yes':
                    deletion = delete_student_data(id)
                    print(deletion)
                elif confirm == 'n' or confirm == 'no':
                    print("Make sure before deleting...")
                else:
                    print("Enter a valid choice")

            elif choice == 5:
                print("Thank you !")
                break

            else:
                print("Enter valid choice")
        
        except ValueError:
            print("Please enter a valid choice")



if __name__ == "__main__":
    main()