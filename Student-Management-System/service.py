from database import view_all_data
from database import insert_data
from database import update_student

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

#delete_student()

def get_all_students():
    rows = view_all_data()

    if not rows:
        return "There is no data"
    else:
        return rows
    
def update_student_data(id,new_name,new_marks):
    try:
        id = int(id)
    except ValueError:
        return "Invalid Id"
    
    new_name = new_name.strip()

    if not new_name :
        return "Error : Name cannot be empty"
    if len(new_name) < 3:
        return "Error : Name must be of atleast 3 characters"

    try:
        new_marks = int(new_marks)
    except ValueError:
        return "Invalid marks"
    
    if new_marks < 0 or new_marks > 100:
        return "Error : Enter marks between 0 to 100" 
    
    rows = update_student(id,new_name,new_marks)

    if rows == 0:
        return "Student not found"
    else:
        return "Student data updated successfully!"
