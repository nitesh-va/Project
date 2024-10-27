from teacher.models import Teacher

def run():
    # Get all teachers
    teachers = Teacher.objects.all()

    for teacher in teachers:
        # Fetch the department for the teacher
        department = teacher.dept_name
        
        if department:  # Ensure the department exists
            # Update the school_name in the Teacher model from the Department's school
            old_school = teacher.school_name
            
            teacher.school_name = department.school  # Use the ForeignKey directly
            teacher.save()  # Save the changes
            print(f"Updated teacher {teacher.emp_id}: {old_school} -> {teacher.school_name}")
            

    

