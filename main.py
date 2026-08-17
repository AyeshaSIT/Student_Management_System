from student_manager import(
    add_student,
    list_students,
    search_student,
    delete_student,
    update_student
)


while True:
    try:
        choice = int(input("================================\nStudent Management System\n================================\n1. Add Student\n2. List Students\n3. Search Student\n4. Update Student\n5. Delete Student\n0. Exit\n"))
    except ValueError:
        print("Enter a valid integer number")
        continue
    if choice==1:
        add_student()
    elif choice==2:
        list_students()
    elif choice==3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
    elif choice==0:
        print("Thanks for using Student Management System")
        break  
    else:
        print("Invalid Choice. Select from upper choices")