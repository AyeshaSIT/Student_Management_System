import json
def load_students():
    """        Load students from students.json.
        Returns:
            list: List of student dictionaries.
        """
    try: 
        with open("students.json","r") as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []


def save_students(students_data):
    """
    Save students to students.json.
    """
    try:
        with open("students.json","w") as file:
            json.dump(students_data,file,indent=4)
            print("Students data saved successfully.")
    except Exception as e:
       print(f"Error saving students data: {e}")

# print(load_students())