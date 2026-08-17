from file_handler import load_students,save_students
class NegativeValueError(Exception):
   pass
class ValueOutOfRangeError(Exception):
    pass
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age<0:
                raise NegativeValueError("Value is negative")
            elif age>120:
                raise ValueOutOfRangeError("Value is greater than 120")
            return age
        except ValueError:
            print("Invalid. Please enter a number.")
        except NegativeValueError as e:
            print(e)    
        except ValueOutOfRangeError as e:
            print(e)    

def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter your marks: "))
            if marks<0:
                raise NegativeValueError("Value is negative")
            elif marks>100:
                raise ValueOutOfRangeError("Marks not be greater than 100")
            return marks
        except ValueError:
            print("Invalid. Please enter a number.")
        except NegativeValueError as e:
            print(e)    
        except ValueOutOfRangeError as e:
            print(e) 
                  
            
# Check duplicate roll number
def roll_number_exists(roll_no,existing_data):
        for student in existing_data:
            if student["roll_no"] == roll_no:
                return True
        return False 
def display_student(student):
    print("\n----------------------")
    print("Student Details")
    print("----------------------")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Roll No: {student['roll_no']}")
    print(f"Marks: {student['marks']}")
    print(f"Course: {student['course']}")
    print(f"Section: {student['section']}")
def get_non_empty_input(prompt):
    while True:
        value=input(prompt).strip()
        if not value:
            print("This field cannot be empty.")
        else:
            return value
    


def add_student():
    last_id = 0
    existing_data = load_students()
    # print(existing_data)
    name = get_non_empty_input("Enter your name: ")
    while True:
     roll_no = get_non_empty_input("Enter your roll number: ")
     if roll_number_exists(roll_no,existing_data):
        print("Roll number already belongs to another student.") 
     else:
         break
     # Check highest id
    for student in existing_data:
         last_id = max(last_id, student["id"])

    course = get_non_empty_input("Enter your course: ")
    section = get_non_empty_input("Enter your section: ")
    age= get_valid_age()
    marks = get_valid_marks()
    student = {
        "id": last_id + 1,
        "name": name,
        "age": age,
        "roll_no": roll_no,
        "marks": marks,
        "course": course,
        "section": section
     }
    existing_data.append(student)
    save_students(existing_data)

def list_students():
    existing_data = load_students()
    if not existing_data:
        print("No Record found")
        return
    
    print("ID  |  Name | Roll No")
    for student in existing_data:
        print(f"{student['id']} | {student['name']} | {student['roll_no']}")

    
def search_student():
    # found = False
    roll_no = get_non_empty_input("Enter roll no to search: ")
    existing_data =load_students()
    if not existing_data:
        print("No record found")
        return
    for student in existing_data:
        if student["roll_no"]==roll_no:
            display_student(student)
            break
    else:
        print("No result found")


def delete_student():
    roll_no = get_non_empty_input("Enter roll no to delete a record:")
    existing_data = load_students()
    if not existing_data:
        print("No record found")
        return
    for student in existing_data:
        if student['roll_no']==roll_no:
            existing_data.remove(student)
            print("Deleted successfully") 
            save_students(existing_data)
            break
    else:
        print("Student not found")
def update_student_record(student,existing_data):
    display_student(student)
    while True:
        try:
         choice= int(input("What you wanna update?\n1. Update Name\n2. Update Age\n3. Update Roll Number\n4. Update Marks\n5. Update Course\n6. Update Section\n0. Cancel\n"))
        except ValueError:
            print("Wrong value.Choose from the above options")
            continue
        if choice==1:
            print(f"Current name: {student['name']}")
            name= get_non_empty_input("Enter name to update:")
            student['name']=name
            print("Name Updated")
            save_students(existing_data)
            
        elif choice==2:
            print(f"Current Age: {student['age']}")
            age = get_valid_age()
            student['age']=age
            print("Age Updated")
            save_students(existing_data)
        elif choice==3:
            print(f"Current Roll No: {student['roll_no']}")
            roll_no= get_non_empty_input("Enter roll_no to update:")
            if student["roll_no"]==roll_no:
                print("This is already the student's current roll number.")
                continue
            if roll_number_exists(roll_no,existing_data):
                    print("Roll number already belongs to another student.")
                    continue 
            student['roll_no']=roll_no
            save_students(existing_data)
            print("Roll No Updated")
        elif choice==4:
            print(f"Current Marks: {student['marks']}")
            marks = get_valid_marks()
            student['marks']=marks
            print("Marks Updated")
            save_students(existing_data)
                    
        elif choice==5:
            print(f"Current Course: {student['course']}")
            course= get_non_empty_input("Enter course to update:")
            student['course']=course
            print("Course Updated")
            save_students(existing_data)
        elif choice==6:
            print(f"Current Section: {student['section']}")
            section= get_non_empty_input("Enter section to update:")
            student['section']=section
            print("section Updated")
            save_students(existing_data)
        elif choice==0:
            print("Update cancelled.")
            break
        else:
            print("Wrong input")
        

def update_student():
    roll_no = get_non_empty_input("Enter roll no to update a record:")
    existing_data = load_students()
    if not existing_data:
        print("No record found")
        return
    for student in existing_data:
        if student['roll_no']==roll_no:
            update_student_record(student,existing_data)
            break
    else:
        print("Student not found")      