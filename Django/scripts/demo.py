from teacher.models import Teacher

def run():
    # Get all teachers
    teachers = Teacher.objects.all()

    for teacher in teachers:
        # Fetch the department for the teacher
        department = teacher.dept_name
        # Ensure the department exists
        if department:  
            # Update the school_name in the Teacher model from the Department's school
            old_school = teacher.school_name
            # Use the ForeignKey directly
            teacher.school_name = department.school  
            # Save the changes
            teacher.save()  
            print(f"Updated teacher {teacher.emp_id}: {old_school} -> {teacher.school_name}")
            

    

