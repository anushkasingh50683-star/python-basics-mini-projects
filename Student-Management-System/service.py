from database import view_all_data
from database import insert_data

def add_student(name,marks):
    name = name.strip()

    if not name :
        return "Error : Name cannot be empty"
    if len(name) < 3:
        return "Error : Name must be of atleast 3 characters"
    
    try:
        marks = int(marks)
    except ValueError:
        return "Error : Enter valid marks"

    if marks < 0 or marks > 100:
        return "Error : Enter marks betweent (0 to 100)"

    insert_data(name,marks)

    return "Data entered successfully!"

#update_student_marks()
#delete_student()

def get_all_students():
    rows = view_all_data()

    if not rows:
        return "There is no data"
    else:
        return rows
    